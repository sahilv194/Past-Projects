from flask import render_template, redirect, flash, url_for
from base import app
from base.com.dao.attendence_dao import AttendanceDAO
from base.service.detect import recognize_and_log_attendance
from base.com.dao.student_dao import StudentDAO
from base.com.vo.attendance_vo import AttendanceVO
from datetime import datetime

@app.route('/admin/insert_attendance')
def insert_attendance():
    folder_path = "base/static/adminResources/upload_folder/"
    attendance_data = recognize_and_log_attendance(folder_path)

    for data in attendance_data:
        detected_name = data['name']
        detected_timestamp = data['timestamp']

        student_name_parts = detected_name.split('.')[0].split('_')

        if len(student_name_parts) != 2:
            flash(f"Invalid name format detected: {detected_name}", "danger")
            continue

        first_name = student_name_parts[0]
        last_name = student_name_parts[1]

        student_dao = StudentDAO()
        student_vo = student_dao.get_student_by_full_name(first_name, last_name)

        if student_vo:
            attendance_vo = AttendanceVO()
            attendance_vo.attendence_status = 1
            attendance_vo.attendence_date = datetime.now().date()
            attendance_vo.attendence_time = datetime.now().time()
            attendance_vo.attendence_student_id = student_vo.student_id

            attendance_dao = AttendanceDAO()
            attendance_dao.insert_attendance(attendance_vo)
        else:
            print(">>>>>>> student_vo is empty >>>>>>>")

    return render_template('admin/studentDashboard.html')

@app.route('/admin/view_attendance')
def admin_view_attendance():
    attendance_dao = AttendanceDAO()
    attendance_list = attendance_dao.view_attendance_with_course()

    attendance_vo_list = []
    for attendance, student, course in attendance_list:
        attendance_vo = {
            'date': attendance.attendence_date,
            'time': attendance.attendence_time.strftime('%H:%M:%S'),
            'student_name': f"{student.first_name} {student.last_name}",
            'course_name': course.course_name,
            'roll_no': student.roll_no,
            'status': "Present" if attendance.attendence_status == 1 else "Absent"
        }
        attendance_vo_list.append(attendance_vo)

    return render_template('admin/ViewAttendence.html', attendance_vo_list=attendance_vo_list)