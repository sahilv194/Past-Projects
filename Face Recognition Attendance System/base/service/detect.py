import face_recognition
import cv2
import os
import numpy as np
from datetime import datetime
import time


def load_known_faces_from_folder(folder_path):
    """Optimized loading of known faces with progress tracking"""
    print(f"Loading known faces from {folder_path}...")
    start_time = time.time()

    known_face_encodings = []
    known_face_names = []

    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    total_images = len(image_files)

    if total_images == 0:
        print("No images found in the specified folder!")
        return [], []

    print(f"Found {total_images} images to process...")

    for i, image_name in enumerate(image_files, 1):
        image_path = os.path.join(folder_path, image_name)
        try:
            image = face_recognition.load_image_file(image_path)
            face_locations = face_recognition.face_locations(image)

            if face_locations:
                face_encoding = face_recognition.face_encodings(image, face_locations)[0]
                known_face_encodings.append(face_encoding)
                known_face_names.append(os.path.splitext(image_name)[0])

                if i % 10 == 0 or i == total_images:
                    print(f"Processed {i}/{total_images} images...")
            else:
                print(f"No face found in {image_name} - skipping")

        except Exception as e:
            print(f"Error processing {image_name}: {str(e)}")

    elapsed = time.time() - start_time
    print(f"Loaded {len(known_face_encodings)} face encodings in {elapsed:.2f} seconds")
    return known_face_encodings, known_face_names


def recognize_and_log_attendance(folder_path, detection_interval=2, duration=5):
    """Face recognition for limited duration (default 5 seconds)"""
    known_face_encodings, known_face_names = load_known_faces_from_folder(folder_path)

    if not known_face_encodings:
        print("No valid face encodings found. Exiting.")
        return []

    video_capture = cv2.VideoCapture(0)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    frame_count = 0
    detected_names_set = set()
    attendance_records = []
    face_locations = []
    face_names = []
    fps = 0

    print(f"Starting face recognition for {duration} seconds...")

    overall_start_time = time.time()
    fps_start_time = time.time()

    while True:
        current_time = time.time()
        if current_time - overall_start_time > duration:
            print(f"\n⏱ Finished scanning after {duration} seconds.")
            break

        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame_count += 1
        if frame_count % 10 == 0:
            fps = 10 / (time.time() - fps_start_time)
            fps_start_time = time.time()

        process_this_frame = frame_count % detection_interval == 0

        if process_this_frame:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_names = []

            if face_locations:
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    name = "Unknown"

                    if matches[best_match_index] and face_distances[best_match_index] < 0.6:
                        name = known_face_names[best_match_index]

                    face_names.append(name)

                updated_face_names = []
                for i, name in enumerate(face_names):
                    if name != "Unknown":
                        if name not in detected_names_set:
                            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            confidence = 1 - face_distances[i] if i < len(face_distances) else 0.0
                            print(f"✅ Detected: {name} at {timestamp} (Confidence: {confidence:.2f})")
                            attendance_records.append({
                                "name": name,
                                "timestamp": timestamp,
                                "confidence": confidence
                            })
                            detected_names_set.add(name)
                            updated_face_names.append(name)
                        else:
                            updated_face_names.append(f"{name} (Present)")
                    else:
                        updated_face_names.append(name)

                face_names = updated_face_names

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 1)

        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow('Face Recognition Attendance', frame)

        # Use waitKey just to keep window responsive
        cv2.waitKey(1)

    video_capture.release()
    cv2.destroyAllWindows()
    return attendance_records


if __name__ == "__main__":
    known_faces_folder = "base/static/adminResources/upload_folder"
    attendance_records = recognize_and_log_attendance(known_faces_folder, detection_interval=2, duration=5)

    print("\n📋 Attendance Summary:")
    for record in attendance_records:
        print(f"{record['name']} - {record['timestamp']} (Confidence: {record['confidence']:.2f})")
