# import os
# import pandas as pd
# from flask import render_template, redirect, flash, url_for, request
# from base import app
# from werkzeug.utils import secure_filename
#
# from base.com.vo.timetable_vo import TimeTableVO
# from base.service.excel_convert_utils import parse_excel_to_dict
# from base.com.dao.timetable_dao import TimeTableDAO
#
# time_table_folder = "base/static/adminResources/time_table_sheet/"
# app.config['time_table_folder'] = time_table_folder
#
#
# @app.route('/admin/load_time_table')
# def admin_load_time_table():
#     return render_template('admin/addTimeTable.html')
#
#
# @app.route('/admin/insert_time_table',methods=['POST'])
# def admin_insert_time_table():
#     time_table_sheet = request.files.get('timeTableFile')
#
#     time_table_sheet_name = secure_filename(time_table_sheet.filename)
#     file_path = os.path.join(app.config['time_table_folder'])
#     time_table_sheet.save(os.path.join(file_path, time_table_sheet_name))
#
#     # time_table_dao=TimetableDAO()
#     source=file_path+time_table_sheet_name
#     print(">>>>>>>>>>>>>>>>",source)
#
#     data = parse_excel_to_dict(source)
#     print("Final Parsed Data >>>>", data)
#
#     for row in data:
#         timetable_vo = TimeTableVO(
#             date=row['date'],
#             subject_name=row['subject_name'],
#             day_of_week=row['day_of_week'],
#             start_time=row['start_time'],
#             end_time=row['end_time'],
#             timetable_filename=source.split('/')[-1],
#             timetable_path=source
#         )
#
#         timetable_dao = TimeTableDAO()
#         timetable_dao.insert_timetable(timetable_vo)
#
#     return redirect(url_for('admin_view_time_table'))
#
#
# @app.route('/admin/view_time_table')
# def admin_view_time_table():
#     timetable_dao = TimeTableDAO()
#     timetable_vo_list=timetable_dao.view_timetables()
#     return render_template('admin/viewTimeTable.html', timetable_vo_list=timetable_vo_list)
#
# @app.route('/admin/delete_timetable')
# def admin_delete_timetable():
#     timetable_dao = TimeTableDAO()
#     timetable_vo=TimeTableVO()
#     timetable_vo = TimeTableVO.query.get(timetable_vo.timetable_id)
#     timetable_id= request.args.get('timetableId')
#
#
#     timetable_dao.delete_timetable(timetable_vo)
#     return redirect('/admin/view_time_table',timetable_vo_list=timetable_vo_list)
import os
import pandas as pd
from flask import render_template, redirect, flash, url_for, request
from base import app
from werkzeug.utils import secure_filename

from base.com.vo.timetable_vo import TimeTableVO
from base.service.excel_convert_utils import parse_excel_to_dict
from base.com.dao.timetable_dao import TimeTableDAO

time_table_folder = "base/static/adminResources/time_table_sheet/"
app.config['time_table_folder'] = time_table_folder


@app.route('/admin/load_time_table')
def admin_load_time_table():
    return render_template('admin/addTimeTable.html')


@app.route('/admin/insert_time_table', methods=['POST'])
def admin_insert_time_table():
    time_table_sheet = request.files.get('timeTableFile')

    if not time_table_sheet:
        flash('No file uploaded!', 'error')
        return redirect(url_for('admin_load_time_table'))

    time_table_sheet_name = secure_filename(time_table_sheet.filename)
    if not time_table_sheet_name.lower().endswith(('.xls', '.xlsx')):
        flash('Only Excel files are allowed!', 'error')
        return redirect(url_for('admin_load_time_table'))

    file_path = os.path.join(app.config['time_table_folder'])
    os.makedirs(file_path, exist_ok=True)
    time_table_sheet.save(os.path.join(file_path, time_table_sheet_name))

    source = os.path.join(file_path, time_table_sheet_name)

    try:
        data = parse_excel_to_dict(source)
        if not data:
            flash('No valid data found in the Excel file!', 'error')
            return redirect(url_for('admin_load_time_table'))

        for row in data:
            timetable_vo = TimeTableVO(
                date=row['date'],
                subject_name=row['subject_name'],
                day_of_week=row['day_of_week'],
                start_time=row['start_time'],
                end_time=row['end_time'],
                timetable_filename=time_table_sheet_name,
                timetable_path=source
            )

            timetable_dao = TimeTableDAO()
            timetable_dao.insert_timetable(timetable_vo)

        flash('Timetable imported successfully!', 'success')
    except Exception as e:
        flash(f'Error processing file: {str(e)}', 'error')

    return redirect(url_for('admin_view_time_table'))


@app.route('/admin/view_time_table')
def admin_view_time_table():
    timetable_dao = TimeTableDAO()
    timetable_vo_list = timetable_dao.view_timetables()
    return render_template('admin/viewTimeTable.html', timetable_vo_list=timetable_vo_list)


@app.route('/admin/delete_timetable')
def admin_delete_timetable():
    timetable_id = request.args.get('timetableId')
    if not timetable_id:
        flash('No timetable selected for deletion!', 'error')
        return redirect(url_for('admin_view_time_table'))

    try:
        timetable_dao = TimeTableDAO()
        timetable_vo = TimeTableVO()
        timetable_vo.timetable_id = timetable_id
        timetable_vo = timetable_dao.delete_timetable(timetable_vo)

        # Remove the associated file if needed
        if timetable_vo and timetable_vo.timetable_path:
            try:
                if os.path.exists(timetable_vo.timetable_path):
                    os.remove(timetable_vo.timetable_path)
            except Exception as e:
                app.logger.error(f"Error deleting file: {str(e)}")

        flash('Timetable deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting timetable: {str(e)}', 'error')

    return redirect(url_for('admin_view_time_table'))


@app.route('/admin/edit_timetable')
def admin_edit_timetable():
    timetable_id = request.args.get('timetableId')
    if not timetable_id:
        flash('No timetable selected for editing!', 'error')
        return redirect(url_for('admin_view_time_table'))

    try:
        timetable_dao = TimeTableDAO()
        timetable_vo = TimeTableVO()
        timetable_vo.timetable_id = timetable_id
        timetable_vo_list = timetable_dao.edit_timetable(timetable_vo)

        if not timetable_vo_list:
            flash('Timetable not found!', 'error')
            return redirect(url_for('admin_view_time_table'))

        return render_template('admin/editTimeTable.html', timetable_vo=timetable_vo_list[0])
    except Exception as e:
        flash(f'Error editing timetable: {str(e)}', 'error')
        return redirect(url_for('admin_view_time_table'))


@app.route('/admin/update_timetable', methods=['POST'])
def admin_update_timetable():
    try:
        timetable_id = request.form.get('timetableId')
        date = request.form.get('date')
        subject_name = request.form.get('subject_name')
        day_of_week = request.form.get('day_of_week')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')

        timetable_vo = TimeTableVO()
        timetable_vo.timetable_id = timetable_id
        timetable_vo.date = date
        timetable_vo.subject_name = subject_name
        timetable_vo.day_of_week = day_of_week
        timetable_vo.start_time = start_time
        timetable_vo.end_time = end_time

        timetable_dao = TimeTableDAO()
        timetable_dao.update_timetable(timetable_vo)

        flash('Timetable updated successfully!', 'success')
    except Exception as e:
        flash(f'Error updating timetable: {str(e)}', 'error')

    return redirect(url_for('admin_view_time_table'))