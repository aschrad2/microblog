# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:09:47 2020

@author: austin.schrader
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models