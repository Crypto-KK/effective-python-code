import numbers


class Field:
    def __init__(self, max_length=None, min_length=None,
                 verbose_name=None):
        self._value = None

        if verbose_name:
            self._internal_name = verbose_name
        else:
            self._internal_name = None

        self.max_length = max_length
        self.min_length = min_length

        self.validate_length(self.max_length)
        self.validate_length(self.min_length)

        if self.min_length is not None and self.max_length is not None:
            if self.min_length > self.max_length:
                raise ValueError('min value must be > max length')

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        value = self.validate(value)

        self._value = value

    def validate_length(self, length):
        if length is not None:
            if not isinstance(length, numbers.Integral):
                raise ValueError('must be int')
            elif length < 0:
                raise ValueError('length must > 0')

    def validate(self, value):
        raise NotImplementedError


class CharField(Field):
    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError('must be string')
        if not (self.min_length <= len(value) <= self.max_length):
            raise ValueError('value must between min and max')
        return value


class IntegerField(Field):
    def validate(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int need')
        if not (self.min_length < value < self.max_length):
            raise ValueError('value must between min and max')
        return value



class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                if value.__dict__['_internal_name'] is None:
                    value.__dict__['_internal_name'] = key
                mappings[key] = value

        attrs_meta = attrs.get('Meta', None)
        _meta = {}
        table_name = ''
        if attrs_meta is not None:
            table = getattr(attrs_meta, 'table_name', None)
            if table_name is not None:
                table_name = table
            else:
                table_name = name.lower()

        _meta['table_name'] = table_name
        attrs['_meta'] = _meta
        attrs['mappings'] = mappings
        del attrs['Meta']
        return type.__new__(cls, name, bases, attrs)


class Model(metaclass=ModelMetaClass):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        fields = []
        values = []
        table_name = self._meta['table_name']
        for key, value in self.mappings.items():
            fields.append(key)
            value = getattr(self, key)
            values.append(str(value))
        sql = 'insert into {table} ({fields}) values({values})'.format(
            table=table_name,
            fields=','.join(fields),
            values=','.join("'" + value + "'" for value in values)
        )
        print(sql)


class User(Model):
    name = CharField(min_length=1, max_length=5, verbose_name='username')
    age = IntegerField(min_length=1, max_length=100)

    class Meta:
        table_name = 'user_table'

if __name__ == '__main__':
    user = User(name='li', age=20)
    user.save()