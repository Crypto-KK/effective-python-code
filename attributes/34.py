import json


class BetterSerializable:
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args
        })

registry = {}
def register_class(target_class):
    registry[target_class.__name__] = target_class

def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


class Point2D(BetterSerializable):
    def __init__(self, x, y):
        super(Point2D, self).__init__(x, y)
        self.x = x
        self.y = y

    def __str__(self):
        return f'<x={self.x}, y={self.y}>'

register_class(Point2D)
point = Point2D(2, 3)
data = point.serialize()
print(data)
print(deserialize(data))
print('=' * 100)

'''
使用元类直接注册到registry
'''
print('使用元类实现：')
class Meta(type):
    def __new__(cls, name, bases, attrs):
        cls = super().__new__(cls, name, bases, attrs)
        register_class(cls)
        return cls

class RegisterSerializable(BetterSerializable, metaclass=Meta):
    pass


class Vector2D(RegisterSerializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector2D<x={self.x}, y={self.y}>'

vector = Vector2D(10, 20)
data = vector.serialize()
print(data)
print(deserialize(data))
print('=' * 100)

'''
使用类装饰器实现不用预先注册registry
'''
print('使用类装饰器实现：')
def serializer(cls):
    def wrapper(*args, **kwargs):
        register_class(cls)
        return cls(*args, **kwargs)
    return wrapper

@serializer
class Vector2D(BetterSerializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector2D<x={self.x}, y={self.y}>'

    def __eq__(self, other):
        cls = self.__class__
        if isinstance(other, cls):
            if other.x == self.x and other.y == self.y:
                return True
        return False

vector = Vector2D(10, 20)
print(vector)
data = vector.serialize()
print(data)
print(deserialize(data))


v1 = Vector2D(1, 2)
v2 = Vector2D(1, 2)
print(v1 == v2)

