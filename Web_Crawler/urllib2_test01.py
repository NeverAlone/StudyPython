# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-14 20:23:48
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
网络爬虫
"""

import urllib2

response = urllib2.urlopen('http://www.baidu.com')
html = response.read()
print html






# This is the end
