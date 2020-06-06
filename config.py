import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

USER = os.environ.get('T_USER') or 'test_user'
PASSWORD = os.environ.get('T_PASSWORD') or 'test@123'
DATABASE = os.environ.get('T_DATABASE') or 'tutorial'
HOST = os.environ.get('T_HOST') or 'localhost'
PORT = os.environ.get('T_PORT') or '5432'


class Config(object):
    SECRET_KEY = os.environ.get('T_SECRET_KEY') or 'TRY2GUESS'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    
    '''
    to disable a feature of Flask-SQLAlchemy that I do not need:
    which is to signal the application every time a change is about to be made in the database.
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False 