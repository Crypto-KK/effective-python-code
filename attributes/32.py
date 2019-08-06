

class BrokenDictonary:
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, item):
        print('__getattribute__')
        data_dict = super().__getattribute__('_data')
        return data_dict[item]

    def __getattr__(self, item):
        print('__getattr__')


data = BrokenDictonary({'foo': 3})

print(hasattr(data, 'foo'))
print(getattr(data, 'foo'))


class ValidatingDB:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, item):
        print('__getattribute__')
        try:
            return super(ValidatingDB, self).__getattribute__(item)
        except AttributeError:
            setattr(self, item, 'shabi')
            return 'shabi'


data = ValidatingDB()
print(data.exists)
print(data.foo)


