from base import db

class CourseVO(db.Model):
    __tablename__ = 'course'
    course_id = db.Column('course_id', db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column('course_name', db.String(255), nullable=False)
    course_description = db.Column('course_description', db.String(255), nullable=False)

    def as_dict(self):
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'course_description': self.course_description,
        }

db.create_all()