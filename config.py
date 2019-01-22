# -*- coding : utf-8 -*-
import os

class Config:
    SECRET_KEY = 'HARD TO GUESS'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_MAIL_SUBJECT_PREFIX = '[Flask]'
    FLASK_MAIL_SENDER = 'FLASK ADMIN <%s>' % os.getenv('MAIL_USERNAME')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    MESSAGE_PER_PAGE = 30
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = '465'
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:0827@localhost:3306/user_form?charset=utf8'

class TestingConfig(Config):
    TESTING = True
    #相同数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:0827@localhost:3306/user_form?charset=utf8'

class ProductionConfig(Config):
    #相同的数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:0827@localhost:3306/user_form?charset=utf8'


config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig,
}

'''
SQLALCHEMY_TRACK_MODIFICATIONS = False
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = '465'
MAIL_USE_SSL = True
MAIL_USE_TLS = False
'''