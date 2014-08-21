# -*- coding: utf-8 -*-


"""
    python2.7.6
    @lonley
    动态创建类

"""


# metaclass是创建类，必须由type类型派生
class ListMetaclass(type):
    """docstring for ListMetaclass"""
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list):
    """docstring for MyList"""
    __metaclass__ = ListMetaclass  # 指示使用ListMetaclass来定制类
    # 指示python解释器在创建MyList时,要通过ListMetaclass.__new__()来创建


L = MyList()
L.add(1)
print L
L.add(2)
print L

print(type(L))

#This is the end
