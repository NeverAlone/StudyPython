# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-15 15:24:51
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
"""

import mysql.connector


conn = mysql.connector.connect(user='root', password='password',
                               database='test', use_unicode=True)

cursor = conn.cursor()
cursor.execute('create table dance1 (id varchar(20) primary key,' +
               'name varchar(20))')
cursor.execute('insert into dance1 (id, name) values (%s, %s)',
               ['1', 'bidandan'])
print cursor.rowcount

# This is the end
