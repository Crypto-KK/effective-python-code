from weakref import WeakKeyDictionary
class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('must 0-100')
        self._values[instance] = value


class Exam:
    a = Grade()
    b = Grade()


exam1 = Exam()
exam2 = Exam()
exam1.a = 20
exam1.b = 30
exam2.a = 40
exam2.b = 60
print(exam1.a)
print(exam2.a)
