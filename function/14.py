def divide(a, b):
    try:
        return  a / b
    except ZeroDivisionError as e:
        raise ValueError('invalid a') from e


print(divide(3, 0))