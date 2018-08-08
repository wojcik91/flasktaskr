import os

# grab the folder where the script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
WTF_SCRF_ENABLED = True
SECRET_KEY = 'ZM5FqD8WZgF@y%KhpC9X'
DEBUG = True

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database URI
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
