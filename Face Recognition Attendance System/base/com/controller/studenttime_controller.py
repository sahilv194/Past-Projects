import os
import pandas as pd
from flask import render_template, redirect, flash, url_for, request
from base import app
from werkzeug.utils import secure_filename

from base.com.vo.timetable_vo import TimeTableVO
from base.service.excel_convert_utils import parse_excel_to_dict
from base.com.dao.timetable_dao import TimeTableDAO


@app.route('/student/time_table')
def view_time_table():
    timetable_dao = TimeTableDAO()
    timetable_vo_list=timetable_dao.view_timetables()
    return render_template('student/viewStudentTimeTable.html', timetable_vo_list=timetable_vo_list)
