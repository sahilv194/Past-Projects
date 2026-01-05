from base import db
from base.com.vo.attendance_vo import AttendanceVO
from base.com.vo.student_vo import StudentVO
from base.com.vo.course_vo import CourseVO

class AttendanceDAO:
    def insert_attendance(self, attendance_vo):
        db.session.add(attendance_vo)
        db.session.commit()

    def view_attendance(self):
        attendance_list = db.session.query(AttendanceVO, StudentVO)\
                           .join(StudentVO, AttendanceVO.attendence_student_id == StudentVO.student_id)\
                           .all()
        return attendance_list

    def view_attendance_with_course(self):
        attendance_list = db.session.query(AttendanceVO, StudentVO, CourseVO)\
                           .join(StudentVO, AttendanceVO.attendence_student_id == StudentVO.student_id)\
                           .join(CourseVO, StudentVO.course_id == CourseVO.course_id)\
                           .all()
        return attendance_list

    def count_attendance(self):
        count_attendance = db.session.query(AttendanceVO).count()
        return count_attendance