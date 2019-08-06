
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

def gen_index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1



# print(index_words('i love you'))

gen = gen_index_words('i love you')
from _collections_abc import Generator
from collections.abc import Generator
print(isinstance(gen, Generator))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))