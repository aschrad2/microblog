# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:09:47 2020

@author: austin.schrader
"""

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Austin'}
    return  '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''