# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-14 14:53:07
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


from wsgiref.simple_server import make_server
from hello import application


httpd = make_server('', 8000, application)
print "Serving HTTP on port 8000..."

httpd.serve_forever()
# This is the end
