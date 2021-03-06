# -*- coding: utf-8 -*-


"""
    python2.7.6
    @lonley
    动态创建类
    未理解，待解决

"""


"""
编写底层模块的第一步，就是先把调用接口写出来。
比如，使用者如果使用这个ORM框架，想定义一个User
类来操作对应的数据库表User，我们期待他写出这样的代码：
"""


class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库
u.save()


"""
其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，
剩下的魔术方法比如save()全部由metaclass自动完成。虽然metaclass的编写
会比较复杂，但ORM的使用者用起来却异常简单
"""


# 首先来定义Field类，它负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等
class StringField(Field):
    """docstring for StringField"""
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    """docstring for IntegerField"""
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    """docstring for ModelMetaclass"""
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name  # 假设表名和类名一致
        attrs['__mappings__'] = mappings  # 保存属性和列表的映射关系
        return type.__new__(cls, name, bases, attrs)


# 基类
class Model(dict):
    __mateclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr(self, key):
        try:
            return self[key]
        except KeyError:
            raise ArithmeticError(r"'Model' object has no attributs '%s'" %
                                  key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(gatattr(self, k, None))
        sql = 'insert into %s (%s) value (%s)' % (self.__table__,
                                                  ','.join(fields),
                                                  ','.join(fields))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

# This is the end
