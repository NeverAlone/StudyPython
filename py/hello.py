# -*- coding: utf-8 -*-
"""
    @lonley
    @PYTHON2.7.6
"""


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


print (type(Hello))


# def fn(self, name='world'):  # 先定义函数
#     print('Hello, %s.' % name)

# Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
# h = Hello()
# h.hello()

# This is the end
