from flask import request, render_template, redirect
from base import app
from base.com.dao.course_dao import CourseDAO
from base.com.vo.course_vo import CourseVO


@app.route('/admin/load_course')
def admin_load_course():
    return render_template('admin/addCourse.html')


@app.route('/admin/insert_course', methods=['POST'])
def admin_insert_course():
    course_name = request.form.get('courseName')
    course_description = request.form.get('courseDescription')

    course_vo = CourseVO()
    course_vo.course_name = course_name
    course_vo.course_description = course_description

    course_dao = CourseDAO()
    course_dao.insert_course(course_vo)

    return redirect('/admin/view_course')


@app.route('/admin/view_course')
def admin_view_course():
    course_dao = CourseDAO()
    course_vo_list = course_dao.view_courses()
    return render_template('admin/viewCourse.html', course_vo_list=course_vo_list)


@app.route('/admin/delete_course')
def admin_delete_course():
    course_vo = CourseVO()
    course_dao = CourseDAO()

    course_id = request.args.get('courseId')
    course_vo.course_id = course_id

    course_dao.delete_course(course_vo)
    return redirect('/admin/view_course')


@app.route('/admin/edit_course', methods=['GET'])
def admin_edit_course():
    course_vo = CourseVO()
    course_dao = CourseDAO()

    course_id = request.args.get('courseId')
    course_vo.course_id = course_id

    course_vo_list = course_dao.edit_course(course_vo)
    return render_template('admin/editCourse.html', course_vo_list=course_vo_list)


@app.route('/admin/update_course', methods=['POST'])
def admin_update_course():
    course_id = request.form.get('courseId')
    course_name = request.form.get('courseName')
    course_description = request.form.get('courseDescription')

    course_vo = CourseVO()
    course_dao = CourseDAO()

    course_vo.course_id = course_id
    course_vo.course_name = course_name
    course_vo.course_description = course_description

    course_dao.update_course(course_vo)
    return redirect('/admin/view_course')
