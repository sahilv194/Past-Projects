from flask import request, render_template, redirect, url_for, session, flash
from base import app
from base.com.dao.attendence_dao import AttendanceDAO
from base.com.dao.student_dao import StudentDAO
from functools import wraps

# Custom login_required decorator (defined directly here)
def login_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'login_role' not in session or session['login_role'] != role:
                return redirect(url_for('admin_load_login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


@app.route('/')
def admin_load_login():
    return render_template('admin/login.html')


@app.route('/admin/home')
@login_required('admin')
def admin_home():
    student_dao = StudentDAO()
    attendance_dao = AttendanceDAO()
    count_student = student_dao.count_student()
    count_attendance = attendance_dao.count_attendance()
    return render_template('admin/index.html',
                           count_student=count_student,
                           count_attendance=count_attendance)


@app.route('/home')
def home():
    student_dao = StudentDAO()
    attendance_dao = AttendanceDAO()
    count_student = student_dao.count_student()
    count_attendance = attendance_dao.count_attendance()
    return render_template('admin/index.html',
                           count_student=count_student,
                           count_attendance=count_attendance)


@app.route('/admin/logout')
def admin_logout():
    session.clear()
    flash('You have been logged out successfully!', 'success')  # Flash message for logout
    return redirect(url_for('admin_load_login'))


@app.route('/student_dashboard')
def student_dashboard():
    return render_template('admin/studentDashboard.html')


@app.route('/admin/validate_login', methods=['POST'])
def admin_validate_login():
    email = request.form.get('email')
    password = request.form.get('password')

    # Simple validation for email and password
    if email == 'admin@gmail.com' and password == 'admin@123':
        session['login_role'] = 'admin'
        flash('Login successful!', 'success')  # Flash message for successful login
        return redirect(url_for('admin_home'))
    else:
        flash('Invalid email or password', 'danger')  # Flash message for failed login
        return render_template('admin/login.html')
