

# class Field:
#     def __init__(self, name):
#         self.name = name
#         self._internal_name = '_' + self.name
#
#     def __get__(self, instance, owner):
#         if instance is None: return self
#         return getattr(instance, self._internal_name, '')
#
#     def __set__(self, instance, value):
#         setattr(instance, self._internal_name, value)
#
#
# class Customer:
#     first = Field('first')
#     second = Field('second')
#
# customer = Customer()
# print(customer.__dict__)
# customer.first = 'abc'
# print(customer.__dict__)

'''
使用元类动态获取属性
'''

class Meta(type):
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if isinstance(value, Field):
                value.name = key
                value._internal_name = '_' + key
        return super().__new__(cls, name, bases, attrs)


class Field:
    def __init__(self):
        self.name = None
        self._internal_name = None

    def __get__(self, instance, owner):
        if instance is None: return self
        return getattr(instance, self._internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self._internal_name, value)


class Row(metaclass=Meta):
    pass

class BetterCustomer(Row):
    first = Field()
    second = Field()

c = BetterCustomer()
c.first = 1
print(c.first)
print(c.__dict__)