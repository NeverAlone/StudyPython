# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-15 09:16:35
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
网络爬虫
"""


import urllib2


req = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
# This is the end
