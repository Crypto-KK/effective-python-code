from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args}, {kwargs}) -> {result}')
        return result
    return wrapper

@trace
def fib(n):
    ''':return 0 1 1 2 3 5 7 12...'''
    if n in (0, 1):
        return n
    return fib(n - 2) + fib(n - 1)


print(fib(3))
