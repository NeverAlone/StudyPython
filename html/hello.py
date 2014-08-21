# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-14 14:49:29
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'

# This is the end
