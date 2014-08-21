# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-20 20:03:56
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
python中__get__,__getattr__,__getattribute__的区别

__get__,__getattr__和__getattribute都是访问属性的方法，但不太相同。 
object.__getattr__(self, name) 
当一般位置找不到attribute的时候，会调用getattr，返回一个值或AttributeError异常。 

object.__getattribute__(self, name) 
无条件被调用，通过实例访问属性。如果class中定义了__getattr__()，则__getattr__()不会被调用（除非显示调用或引发AttributeError异常） 

object.__get__(self, instance, owner) 
如果class定义了它，则这个class就可以称为descriptor。owner是所有者的类，instance是访问descriptor的实例，如果不是通过实例访问，而是通过类访问的话，instance则为None。（descriptor的实例自己访问自己是不会触发__get__，而会触发__call__，只有descriptor作为其它类的属性才有意义。）（所以下文的d是作为C2的一个属性被调用） 

"""


class C(object):

    """docstring for C"""
    a = 'abc'

    def __getattribute__(self, *args, **kwargs):
        print '__getattribute__() is called'
        return object.__getattribute__(self, *args, **kwargs)

    def __getattr__(self, name):
        print('__getattr__ is called')
        return name + 'from getattr'

    def __get__(self, instance, owner):
        print('__get__() is called')
        return self

    def foo(self, x):
        print x


class C2(object):
    d = C()

if __name__ == '__main__':
    c = C()
#    print 'c is constructed'
    c2 = C2()
#   print 'c2 is constructed'
    print c.a
    print c.zzzzzzzz
    c2.d
    print c2.d.a
    c.d


"""
"""
# This is the end
