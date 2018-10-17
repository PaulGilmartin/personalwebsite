import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'myKey'
    SQL_LITE_STR = 'sqlite:///'
    _DEFAULT_URI = SQL_LITE_STR + os.path.join(basedir, 'app.db')

    # Flask-SQLAlchemy extension takes the location of the application's database from
    # the uri var below. We use the 'app' db configured in the main directory of this application
    # if no db url defined in the url
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or _DEFAULT_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
