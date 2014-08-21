# -*- coding:utf-8 -*-


"""
    @python2.7.6
    @lonley
    SQLite

"""

# 导入SQLite数据库
import sqlite3
# 连接到数据库
# 数据库文件时test.db
# 如果文件不存在，会自动在当前目录创建


# connection = sqlite3.connect('tes.db')
# # 创建一个Cursor
# cursor = connection.cursor()
# # 执行一条SQL语句，创建user表
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 继续执行一条SQL语句，插入一条记录
# cursor.execute('insert into user (id, name) values (\'2\', \'danner\')')
# # 通过rowcount获得插入的行数
# cursor.rowcount
# # 关闭Cursor
# cursor.close()
# # 提交事务s
# connection.commit()
# # 关闭lianjie
# connection.close()

connect = sqlite3.connect('tes.db')
cursor = connect.cursor()
cursor.execute('select * from user where id=?', '2')
values = cursor.fetchall()
print values
cursor.close()
connect.close()

# This is the end
