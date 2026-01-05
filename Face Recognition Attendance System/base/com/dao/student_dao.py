from base import db
from base.com.vo.course_vo import CourseVO
from base.com.vo.student_vo import StudentVO

class StudentDAO:
    def insert_student(self, student_vo):
        db.session.add(student_vo)
        db.session.commit()

    def view_students(self):
        student_vo_list = db.session.query(StudentVO,CourseVO).join(CourseVO,StudentVO.course_id==CourseVO.course_id).all()
        # student_vo_list = StudentVO.query.all()
        print(student_vo_list,"""""")
        return student_vo_list

    def delete_student(self, student_vo):
        student_vo_list = StudentVO.query.get(student_vo.student_id)
        db.session.delete(student_vo_list)
        db.session.commit()
        return  student_vo_list

    def edit_student(self, student_vo):
        student_vo_list = StudentVO.query.filter_by(student_id=student_vo.student_id).all()
        return student_vo_list

    def update_student(self, student_vo):
        db.session.merge(student_vo)
        db.session.commit()

    def get_student_by_full_name(self, first_name, last_name):
        student_vo = StudentVO.query.filter_by(first_name=first_name, last_name=last_name).first()
        return student_vo

    def count_student(self):
        count_std = StudentVO.query.count()
        print(count_std)
        return count_std