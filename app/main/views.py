#-*- coding : utf-8 -*-
from datetime import datetime, timedelta
from flask import render_template, current_app, redirect, request, url_for, flash
from flask_mail import Message
from flask_login import login_required, login_user, logout_user, current_user
from urllib import parse
from app import mail
from . import main
from .forms import LoginForm, RegistrationForm
from ..models import User
from ..models import Message as Msg
from .. import db   #..为app.__init__
from .. import socketio
from flask_socketio import emit
import pymysql

pymysql.install_as_MySQLdb()


online_users = []

@main.route('/login', methods=['GET', 'POST'])
def login():
    user_amount = User.query.count()
    form = LoginForm()
    global online_users

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            if current_user.email in online_users:
                pass
            else:
                online_users.append(current_user.email)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('无效密码或用户名')

    return render_template('login',
                           user_amount=user_amount,
                           form=form,
                           current_time=datetime.utcnow()
                           )

@main.route('/register', methods=['GET', 'POST'])
def register():
    user_amount = User.query.count()
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, '确认账户', '/mail/confirm_text',
                   'mail/confirm', user=user, token=token)
        flash(u'发送成功')
        return redirect(url_for('main.login'))

    return render_template('register',
                           user_amount=user_amount,
                           form=form,
                           current_time=datetime.utcnow()
                           )

@main.route('/logout')
@login_required
def logout():
    global online_users
    if current_user.email not in online_users:
        pass
    else:
        online_users.remove(current_user.email)
    logout_user()
    flash('已登出')

    return redirect(url_for('main.index'))

@main.route('/user/<name>')
def user(name):
    user_amount = User.query.count()
    user = User.query.filter_by(username=name).first()
    if user is None:
        return index()
    amount = current_app.config['MESSAGE_PER_PAGE']
    messages = Msg.query.order_by(Msg.timestamp.asc())[-amount:]
    return render_template('home',
                           user_amount=user_amount,
                           messages=messages,
                           )

@main.route('/', methods=['GET', 'POST'])
def index():
    user_amount = User.query.count()
    return render_template('user',
                           user_amount=user_amount,
                           )

#socketio部分#
@socketio.on('imessage', namespace='/test_conn')
def test_message(message):
    global online_users
    if current_user.is_authenticated and current_user.email in online_users:
        pass
    elif current_user.is_authenticated and current_user.email not in online_users:
        online_users.append(current_user.email)
    if message['data'] == "":
        pass
    else:
        text = Msg(author=current_user._get_current_object(), message_txt=parse.unquote_plus(message['data']), message_color=parse.unquote_plus(message['msg_color']))
        db.session.add(text)
        db.session.commit()
    emit('message',#后端广播信息的事件名最好跟前端发送信息的事件名不一样
         {'data': (message['data']),
          'message_html':render_template('chatbox/msg_box',message=text),
          'username':current_user.username,
          'usercount':len(online_users),
          'userall':User.query.count(),},
         broadcast=True)

##mail功能
def send_email(to, subject, template_txt, template_html, **kwargs):
    msg = Message('Flasky' + subject,
                  sender='510302764@qq.com',
                  recipients=[to]
                  )

    msg.body = render_template(template_txt, **kwargs)
    msg.html = render_template(template_html, **kwargs)
    mail.send(msg)
