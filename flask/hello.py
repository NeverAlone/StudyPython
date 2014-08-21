# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-19 18:51:48
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
first flask  program
"""

from flask import Flask


app = Flask(__name__)


@app.route('/')  # 路由
def Hello_world():
    return "Hello world,I'm here!"

if __name__ == '__main__':
    app.run(debug=True)


# This is the end
