# -*- coding : utf-8 -*-
from flask import Flask, render_template, redirect, url_for, session, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
from form import NameForm, LoginForm
from config import config

app = Flask(__name__)

app.config.from_object(config['development'])

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
mail = Mail(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')


    def __repr__(self):
        return  '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username



@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login', name=session.get('name'), form=form, current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    user = User.query.filter_by(username=name).first()
    if user is None:
        return index()
    return render_template('home', name=session.get('name'), current_time=datetime.utcnow())


@app.route('/',methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if user is None and email is None:
            user = User(username=form.name.data, email=form.email.data, role_id=2)
            db.session.add(user)
            session['known'] = False
            if User.query.filter_by(email=form.email.data).first():
                send_email(form.email.data, u'测试邮件', 'mail/mailtest', 'mail/mailhtml', name=user.username)
        session['known'] = True
        session['name'] = form.name.data
        form.name.data = ""
        form.email.data = ""

    return render_template(
        'user',
        form=form, name=session.get('name'),
        known=session.get('known', False),
        current_time=datetime.utcnow()
    )

##mail功能
def send_email(to, subject, template_txt, template_html, **kwargs):
    msg = Message(mail.app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=mail.app.config['FLASK_MAIL_SENDER'],
                  recipients=[to])

    msg.body = render_template(template_txt, **kwargs)
    msg.html = render_template(template_html, **kwargs)
    mail.send(msg)


##create_app工厂
'''
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    mail.init_app(app)

    return app
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
