from base import db
from base.com.vo.course_vo import CourseVO


class StudentVO(db.Model):
    __tablename__ = 'student'
    student_id = db.Column('student_id', db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column('first_name', db.String(255), nullable=False)
    last_name = db.Column('last_name', db.String(255), nullable=False)
    dob = db.Column('dob', db.Date, nullable=False)
    address = db.Column('address', db.String(255), nullable=False)
    gender = db.Column('gender', db.String(10), nullable=False)
    mobile = db.Column('mobile', db.String(15), nullable=False)
    email = db.Column('email', db.String(255), nullable=False)
    roll_no = db.Column('roll_no', db.String(50), nullable=False)
    password = db.Column('password', db.String(255), nullable=False)
    course_id = db.Column('course_id', db.Integer,
                          db.ForeignKey(CourseVO.course_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    file_name = db.Column('file_name', db.String(255), nullable=False)
    file_path = db.Column('file_path', db.String(255), nullable=False)

    def as_dict(self):
        return {
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'dob': self.dob,
            'address': self.address,
            'gender': self.gender,
            'mobile': self.mobile,
            'email': self.email,
            'roll_no': self.roll_no,
            'password': self.password,
            'course_id': self.course_id,
            'file_name': self.file_name,
            'file_path': self.file_path
        }


db.create_all()
