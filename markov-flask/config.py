from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# init app
app = Flask(__name__)

# set up base dir and db path
basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, 'db.sqlite')

# set up db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

# init db and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)