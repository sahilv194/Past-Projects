import os
from flask import request, render_template, redirect
from base import app
from werkzeug.utils import secure_filename

from base.com.dao.course_dao import CourseDAO
from base.com.dao.student_dao import StudentDAO
from base.com.vo.student_vo import StudentVO

upload_folder = 'base/static/adminResources/upload_folder/'
app.config['upload_folder'] = upload_folder


@app.route('/admin/load_student')
def admin_load_student():
    course_dao = CourseDAO()
    course_vo_list = course_dao.view_courses()
    print("=========================", course_vo_list)
    return render_template('admin/addStudent.html', course_vo_list=course_vo_list)


@app.route('/admin/insert_student', methods=['POST'])
def admin_insert_student():
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    dob = request.form.get('dob')
    address = request.form.get('address')
    gender = request.form.get('gender')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    roll_no = request.form.get('rollNo')
    password = request.form.get('password')
    student_course = request.form.get('courseName')
    upload_file = request.files.get('upload_file')

    file_name = None
    file_path = None

    if upload_file:
        file_extension = os.path.splitext(secure_filename(upload_file.filename))[1]
        unique_filename = f"{first_name}_{last_name}{file_extension}"

        file_path = os.path.join(app.config['upload_folder'])
        upload_file.save(os.path.join(file_path, unique_filename))

        file_name = unique_filename

    student_vo = StudentVO()
    student_vo.first_name = first_name
    student_vo.last_name = last_name
    student_vo.dob = dob
    student_vo.address = address
    student_vo.gender = gender
    student_vo.mobile = mobile
    student_vo.email = email
    student_vo.roll_no = roll_no
    student_vo.password = password
    student_vo.course_id = student_course
    student_vo.file_name = file_name
    student_vo.file_path = file_path.replace("base", "..") if file_name else None

    student_dao = StudentDAO()
    student_dao.insert_student(student_vo)

    return redirect('/admin/view_student')


@app.route('/admin/view_student')
def admin_view_student():
    student_dao = StudentDAO()
    student_vo_list = student_dao.view_students()
    return render_template('admin/viewStudent.html', student_vo_list=student_vo_list)


@app.route('/admin/delete_student')
def admin_delete_student():
    student_vo = StudentVO()
    student_dao = StudentDAO()

    student_id = request.args.get('studentId')
    student_vo.student_id = student_id

    student_vo_list = student_dao.delete_student(student_vo)

    file_path = os.path.join(student_vo_list.file_path.replace("..", "base"), student_vo_list.file_name)
    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect('/admin/view_student')


@app.route('/admin/edit_student', methods=['GET'])
def admin_edit_student():
    student_vo = StudentVO()
    student_dao = StudentDAO()

    student_id = request.args.get('studentId')
    print(student_id,">>>>>>>>>>>")
    student_vo.student_id = student_id

    student_vo_list = student_dao.edit_student(student_vo)
    print(student_vo_list)
    return render_template('admin/editStudent.html', student_vo_list=student_vo_list)


@app.route('/admin/update_student', methods=['POST'])
def admin_update_student():
    student_id = request.form.get('studentId')
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    dob = request.form.get('dob')
    address = request.form.get('address')
    gender = request.form.get('gender')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    roll_no = request.form.get('rollNo')
    password = request.form.get('password')

    student_vo = StudentVO()
    student_dao = StudentDAO()

    student_vo.student_id = student_id
    student_vo.first_name = first_name
    student_vo.last_name = last_name
    student_vo.dob = dob
    student_vo.address = address
    student_vo.gender = gender
    student_vo.mobile = mobile
    student_vo.email = email
    student_vo.roll_no = roll_no
    student_vo.password = password

    student_dao.update_student(student_vo)
    return redirect('/admin/view_student')
