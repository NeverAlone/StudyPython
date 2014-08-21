# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-20 12:44:57
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
构建URL
"""


from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def Index():
    return 'Index Page'


@app.route('/login')
def Login():
    return 'Login Paege'


@app.route('/user/<username>')
def profile(username):
    return str(username)


with app.test_request_context():
    print url_for('Index')
    print url_for('Login')
    print url_for('Login', next='/')
    print url_for('profile', username='Lonely Green')
# This is the end
