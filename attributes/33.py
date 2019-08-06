
class Meta(type):
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=Meta):
    stuff = 1
    def fuck(self):
        pass


class ValidatePolygon(type):
    def __new__(cls, name, bases, attrs):
        print(bases)
        if bases != ():
            if attrs['sides'] < 3:
                raise ValueError('sides > 3')
        return super().__new__(cls, name, bases, attrs)

class Polygon(metaclass=ValidatePolygon):
    sides = None
    @classmethod
    def angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3

