# from base import db
# from base.com.vo.timetable_vo import TimeTableVO
#
# class TimeTableDAO:
#     def insert_timetable(self, timetable_vo):
#         db.session.add(timetable_vo)
#         db.session.commit()
#
#     def view_timetables(self):
#         timetable_vo_list = TimeTableVO.query.all()
#         return timetable_vo_list
#
#     def delete_timetable(self, timetable_vo):
#         timetable_vo_list = TimeTableVO.query.get(timetable_vo.timetable_id)
#         db.session.delete(timetable_vo_list)
#         db.session.commit()
#         return  timetable_vo_list
#
#     def edit_timetable(self, timetable_vo):
#         timetable_vo_list = TimeTableVO.query.filter_by(timetable_id=timetable_vo.timetable_id).all()
#         return timetable_vo_list
#
#     def update_timetable(self, timetable_vo):
#         db.session.merge(timetable_vo)
#         db.session.commit()
from base import db
from base.com.vo.timetable_vo import TimeTableVO

class TimeTableDAO:
    def insert_timetable(self, timetable_vo):
        db.session.add(timetable_vo)
        db.session.commit()

    def view_timetables(self):
        timetable_vo_list = TimeTableVO.query.order_by(TimeTableVO.date, TimeTableVO.start_time).all()
        return timetable_vo_list

    def delete_timetable(self, timetable_vo):
        timetable_vo_to_delete = TimeTableVO.query.get(timetable_vo.timetable_id)
        if timetable_vo_to_delete:
            db.session.delete(timetable_vo_to_delete)
            db.session.commit()
            return timetable_vo_to_delete
        return None

    def edit_timetable(self, timetable_vo):
        timetable_vo_list = TimeTableVO.query.filter_by(timetable_id=timetable_vo.timetable_id).all()
        return timetable_vo_list

    def update_timetable(self, timetable_vo):
        db.session.merge(timetable_vo)
        db.session.commit()