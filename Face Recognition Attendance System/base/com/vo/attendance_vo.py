from base import db
from base.com.vo.student_vo import StudentVO

class AttendanceVO(db.Model):
    __tablename__ = 'attendence_table'

    attendence_id = db.Column('attendence_id', db.Integer, primary_key=True, autoincrement=True)
    attendence_date = db.Column('attendence_date', db.Date, nullable=False)
    attendence_time = db.Column('attendence_time', db.Time, nullable=False)
    attendence_status = db.Column('attendence_status', db.Integer, nullable=False)
    attendence_student_id = db.Column('attendence_student_id', db.Integer,
                                      db.ForeignKey(StudentVO.student_id,
                                                    ondelete='CASCADE',
                                                    onupdate='CASCADE' ),
                                      nullable=False)

    def as_dict(self):
        return {
            'attendence_id': self.attendence_id,
            'attendence_date': self.attendence_date,
            'attendence_time': self.attendence_time,
            'attendence_status': self.attendence_status,
            'attendence_student_id': self.attendence_student_id,
        }

db.create_all()