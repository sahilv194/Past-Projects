import random
import smtplib
from datetime import timedelta, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from functools import wraps

import bcrypt
import httpagentparser
import jwt
from flask import render_template, redirect, request, url_for, make_response, flash, session

from base import app
from base.com.dao.device_info_dao import DeviceInfoDAO
from base.com.dao.login_dao import LoginDAO
from base.com.vo.login_vo import LoginVO
from base.com.vo.device_info_vo import DeviceInfoVO


def get_client_identity():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    agent = request.environ.get('HTTP_USER_AGENT')
    browser = httpagentparser.detect(agent)
    if not browser:
        browser = agent.split('/')[0]
    else:
        browser = browser['browser']['name']
    return f"{ip_addr}:{browser}"


def insert_client_identity(login_id):
    login_vo = LoginVO()
    login_vo.login_id = login_id

    device_info_dao = DeviceInfoDAO()
    device_info_vo = DeviceInfoVO()

    device_list = device_info_dao.search_device(login_vo)
    for device in device_list:
        if bcrypt.checkpw(get_client_identity().encode("utf-8"),
                          device.device_identity.encode("utf-8")):
            device_info_vo = device
            break

    hashed_client_identity = bcrypt.hashpw(
        get_client_identity().encode("utf-8"),
        bcrypt.gensalt(rounds=12))
    device_info_vo.device_identity = hashed_client_identity
    device_info_vo.device_login_id = login_id
    device_info_dao.insert_device_info(device_info_vo)


def refresh_token(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            refreshtoken = request.cookies.get('refreshtoken')
            if not refreshtoken:
                flash('Unauthorized Access')
                return admin_logout_session()

            data = jwt.decode(refreshtoken, app.config['SECRET_KEY'], algorithms=['HS256'])
            login_vo = LoginVO()
            login_dao = LoginDAO()
            login_vo.login_username = data['public_id']
            login_vo_list = login_dao.check_login_username(login_vo)

            if not login_vo_list:
                flash('Unauthorized Access')
                return admin_logout_session()

            device_info_dao = DeviceInfoDAO()
            device_list = device_info_dao.search_device(login_vo_list[0])

            for device in device_list:
                if bcrypt.checkpw(get_client_identity().encode("utf-8"),
                                  device.device_identity.encode("utf-8")):
                    response = make_response(fn(*args, **kwargs))
                    response.set_cookie('accesstoken',
                                        value=jwt.encode({
                                            'public_id': login_vo_list[0].login_username,
                                            'role': 'admin',
                                            'exp': datetime.utcnow() + timedelta(minutes=15)
                                        }, app.config['SECRET_KEY'], 'HS256'),
                                        max_age=timedelta(minutes=15),
                                        httponly=True,
                                        secure=True,
                                        samesite='Strict')

                    refresh = jwt.encode({
                        'public_id': login_vo_list[0].login_username,
                        'exp': datetime.utcnow() + timedelta(days=1)
                    }, app.config['SECRET_KEY'], 'HS256')

                    response.set_cookie('refreshtoken',
                                        value=refresh,
                                        max_age=timedelta(days=1),
                                        httponly=True,
                                        secure=True,
                                        samesite='Strict')
                    return response

            flash('Security alert: Device mismatch')
            return admin_logout_session(login_vo.login_username)
        except jwt.ExpiredSignatureError:
            flash('Session expired. Please log in again.')
            return admin_logout_session()
        except Exception as ex:
            print('Exception in Refreshing Token', ex)
            flash('Security error occurred')
            return admin_logout_session()

    return wrapper


def login_required(role='admin'):
    def inner(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                accesstoken = request.cookies.get('accesstoken')
                if not accesstoken:
                    return refresh_token(fn)(*args, **kwargs)

                data = jwt.decode(accesstoken, app.config['SECRET_KEY'], algorithms=['HS256'])
                if data.get('role') != role:
                    flash('Unauthorized Access')
                    return admin_logout_session()

                login_vo = LoginVO()
                login_dao = LoginDAO()
                login_vo.login_username = data['public_id']
                login_vo_list = login_dao.check_login_username(login_vo)

                if not login_vo_list or not login_vo_list[0].login_status:
                    flash('Account disabled or unauthorized')
                    return admin_logout_session()

                return fn(*args, **kwargs)

            except jwt.ExpiredSignatureError:
                return refresh_token(fn)(*args, **kwargs)
            except Exception as ex:
                print("Login required exception:", ex)
                flash('Security error occurred')
                return admin_logout_session()

        return decorator

    return inner


@app.route('/admin/validate_login', methods=['POST'])
def admin_validate_login():
    try:
        login_username = request.form.get('email')
        login_password = request.form.get('password').encode("utf-8")

        if not login_username or not login_password:
            flash('Please provide both email and password')
            return redirect('/')

        login_vo = LoginVO()
        login_dao = LoginDAO()
        login_vo.login_username = login_username
        login_vo_list = login_dao.check_login_username(login_vo)

        if not login_vo_list:
            flash('Invalid credentials')
            return redirect('/')

        login_data = login_vo_list[0].as_dict()

        if not login_data['login_status']:
            flash('Account disabled. Contact administrator.')
            return redirect('/')

        if not bcrypt.checkpw(login_password, login_data['login_password'].encode("utf-8")):
            flash('Invalid credentials')
            return redirect('/')

        if login_data['login_role'] != 'admin':
            flash('Unauthorized access')
            return redirect('/')

        insert_client_identity(login_data['login_id'])

        response = make_response(redirect(url_for('admin_home')))
        response.set_cookie('accesstoken',
                            value=jwt.encode({
                                'public_id': login_username,
                                'role': 'admin',
                                'exp': datetime.utcnow() + timedelta(minutes=15)
                            }, app.config['SECRET_KEY'], 'HS256'),
                            max_age=timedelta(minutes=15),
                            httponly=True,
                            secure=True,
                            samesite='Strict')

        refresh = jwt.encode({
            'public_id': login_username,
            'exp': datetime.utcnow() + timedelta(days=1)
        }, app.config['SECRET_KEY'], 'HS256')

        response.set_cookie('refreshtoken',
                            value=refresh,
                            max_age=timedelta(days=1),
                            httponly=True,
                            secure=True,
                            samesite='Strict')
        return response

    except Exception as ex:
        print("admin_validate_login exception:", ex)
        flash('Login error occurred')
        return redirect('/')


@app.route("/admin/logout_session", methods=['GET'])
def admin_logout_session(*user_name):
    try:
        if user_name and user_name[0]:
            login_vo = LoginVO()
            login_dao = LoginDAO()
            device_info_dao = DeviceInfoDAO()

            login_vo.login_username = user_name[0]
            login_vo_list = login_dao.check_login_username(login_vo)

            if login_vo_list:
                device_info_dao.delete_all_device(login_vo_list[0].login_id)

        response = make_response(redirect('/'))
        response.set_cookie('accesstoken', '', max_age=0)
        response.set_cookie('refreshtoken', '', max_age=0)
        session.clear()
        return response

    except Exception as ex:
        print("admin_logout_session exception:", ex)
        response = make_response(redirect('/'))
        response.set_cookie('accesstoken', '', max_age=0)
        response.set_cookie('refreshtoken', '', max_age=0)
        session.clear()
        return response