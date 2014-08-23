# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-20 16:26:44220211199201281526
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
__builtin__模块
"""


#-----------------------------------
"""
 使用元组或字典中的参数调用函数
"""

# 创建函数参数列表. 只要把所有的参数放入一个元组中，然后通过内建的 apply 函数调用函数

"""
def function(a, b):
    print a, b

apply(function, ("dandan", "zhengyue"))
apply(function, (1, 2 + 3))
"""

#  使用 apply函数传递关键字参数

"""
def function(a, b):
    print a, b

apply(function, ("crunchy", "frog"))
apply(function, ("crunchy",), {"b": "frog"})
apply(function, (), {"a": "crunchy", "b": "frog"})

"""


# 使用 apply 函数调用基类的构造函数

"""
class Rectangle():


    def __init__(self, color="white", width=10, height=10):
        print "create a", color, self, "sized", width, "x", height


class RoundedRectangle(Rectangle):

    def __init__(self, **kw):
        apply(Rectangle.__init__, (self,), kw)


rect = Rectangle(color='green', height=100, width=100)
rect = RoundedRectangle(color='blue', height=20)

"""


"""
加载和重载模块
"""


# 使用 _ _import_ _ 函数加载模块

"""
import glob
import os


modules = []

for module_file in glob.glob("*-plugin.py"):
    try:
        module_name, ext = os.path.splitext(os.path.basename(module_file))
        module = __import__(module_name)
        modules.append(module)
    except ImportError:
        pass  # ignore broken mofules


# say hello to all modules
print len(modules)
for module in modules:
    module.hello()


def hello():
    print "example-plugin says hello"

"""


#  使用 _ _import_ _ 函数获得特定函数
"""
def getfunctionbyname(module_name, function_name):
    module = __import__(module_name)
    return getattr(module, function_name)

print repr(getfunctionbyname("dumbdbm", 'open'))
"""

#  使用 _ _import_ _ 函数实现 延迟导入

"""
class LazyImport:

    def __init__(self, module_name):
        self.module_name = module_name
        self.module = None

    def __getattr__(self, name):  # 当通过类访问属性不存在是调用该函数
        print '__getattr__ is called'
        if self.module is None:
            self.module = __import__(self.module_name)
        return getattr(self.module, name)


strin = LazyImport("string")
print strin.lowercase
"""

"""
import re
reload(re)
reload(re)
"""

# 使用 dir 函数查找类的所有成员

"""
class A:

    def a(self):
        pass

    def b(self):
        pass


class B(A):

    def c(self):
        pass

    def d(self):
        pass


def getmembers(klass, members=None):
    if members is None:
        members = []
    for k in klass.__bases__:
        getmembers(k, members)
    for m in dir(klass):
        if m not in members:
            members.append(m)

    return members

print getmembers(A)
print getmembers(B)
"""

# 使用 vars 函数

"""
book = 'library2'
pages = 250
scripts = 350

print 'the %(book)s book contains more than %(scripts)s scripts' % vars()
print 'the %s book contains more than %s scripts' % (book, scripts)
"""

# 检查对象类型

"""
def function(value):
    print value

function(1)
function(1.0)
function("one")


def dump(value):
    print type(value), value


dump(1)
dump(1.0)
dump("one")
"""

# 对文件名和文件对象使用type函数

"""
def load(file):
    if isinstance(file, type("")):
        file = open(file, 'rb')
        return file.read()

print len(load('C:\\Users\\Lonely\\Desktop\\test.py'))
"""


# 使用callable函数

"""
def dump(function):
    if callable(function):
        print function, "is callable"
    else:
        print function, "is not callable"


class A:

    def method(self, value):
        return value


class B(A):

    def __call__(self, value):
        return value

a = A()
b = B()

dump(0)
dump('string')
dump(callable)
dump(dump)

dump(A)
dump(B)
dump(B.method)


dump(a)
dump(b)
dump(b.method)

"""


# 使用isinstance函数

# issubclass 函数在接受非类对象时会引发异常


"""
class A:
    pass


class B:
    pass


class C(A):
    pass


class D(A, B):
    pass


def dump(object):
    print object, "=>",
    if isinstance(object, A):
        print "A",
    if isinstance(object, B):
        print "B",
    if isinstance(object, C):
        print "C",
    if isinstance(object, D):
        print "D",
    print


a = A()
b = B()
c = C()
d = D()

dump(a)
dump(b)
dump(c)
dump(d)

"""

# 使用eval函数


def dump(expression):
    result = eval(expression)
    print expression, "=>", result, type(result)


# dump('1')
# dump('1.0')
# dump("'string'")
# dump('1.0 + 2.0')
# dump("'*' * 10")
# dump("len('world')")


# print eval("__import__('os').getcwd()")
# print eval("__import__('os').remove('file')", {"__builtins__": {}})


# 从 _ _builtin_ _ 模块重载函数

# 显式地访问 _ _builtin__ 模块中的函数
# This is the end
