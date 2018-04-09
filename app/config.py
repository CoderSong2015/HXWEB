#Configuration file

import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'xx <403438485@qq.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/song?'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    pass

config = {
    'default' : DevelopmentConfig
}

