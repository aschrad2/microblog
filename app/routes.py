# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:09:47 2020

@author: austin.schrader
"""

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Austin'}
    return render_template('index.html', title='Home', user=user)