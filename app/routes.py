# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:09:47 2020

@author: austin.schrader
"""

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"