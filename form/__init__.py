# -*- coding : utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Regexp, length, Email

class NameForm(FlaskForm):
    name = StringField('What is your name', validators=[DataRequired(),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'name is invalid')])
    email = StringField('Email', validators=[DataRequired(), length(1, 64), Email()])
    submit = SubmitField('Submit')
# email=form.email.data,    email = StringField('Email', validators=[DataRequired(),length(1,64),Email()])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),length(1,64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')