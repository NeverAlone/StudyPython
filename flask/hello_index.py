# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-19 19:55:29
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
路由
"""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page."


@app.route("/hello")
def Hello():
    return "Hello, dandan!!!"


@app.route('/user/<username>')
def show_user_profile(username):
    return "Welcom danner"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return post_id


@app.route('/projects/')
def projects():
    return 'My projects'


@app.route('/about/')
def about():
    return "lonely's Flask"


if __name__ == '__main__':
    app.run(debug=True)
# This is the end
