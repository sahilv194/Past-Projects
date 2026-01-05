from base import db
from datetime import date, time

class TimeTableVO(db.Model):
    __tablename__ = 'timetable_table'
    timetable_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    subject_name = db.Column(db.String(255), nullable=False)
    day_of_week = db.Column(db.String(20), nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    timetable_filename = db.Column(db.String(255))
    timetable_path = db.Column(db.String(255))

    def to_dict(self):
        return {
            'timetable_id': self.timetable_id,
            'date': self.date.isoformat() if self.date else None,
            'subject_name': self.subject_name,
            'day_of_week': self.day_of_week,
            'start_time': self.start_time.strftime('%H:%M') if self.start_time else None,
            'end_time': self.end_time.strftime('%H:%M') if self.end_time else None,
            'timetable_filename': self.timetable_filename,
            'timetable_path': self.timetable_path
        }
db.create_all()