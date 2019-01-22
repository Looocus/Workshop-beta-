# -*- coding : utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Regexp, length, Email, EqualTo
from ..models import User


class NameForm(FlaskForm):
    name = StringField('What is your name',
                       validators=[DataRequired(),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'name is invalid')],
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
# email=form.email.data,    email = StringField('Email', validators=[DataRequired(),length(1,64),Email()])


class LoginForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(),length(1,64), Email()],
                        render_kw={"placeholder": "Your email",
                                   "style": "text-indent: 28px"},
                        )
    password = PasswordField("Password",
                             validators=[DataRequired()],
                             render_kw={"placeholder": "Password",
                                        "style": "text-indent: 28px"},)
    remember_me = BooleanField(u'记住密码')
    submit = SubmitField(u'登录')


class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), length(1,64), Email()])

    username = StringField('Username', validators=[DataRequired(), length(1,64),
                                                   Regexp('^[\u4e00-\u9fa5_a-zA-Z0-9]+$',
                                                          0, '只能中文、英文和数字')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='密码必须一致')
    ])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')


    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')