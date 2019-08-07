import logging
from contextlib import contextmanager


logger = logging.getLogger()

def my_function():
    logging.debug('debug')
    logging.error('error')


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


with debug_logging(logging.DEBUG):
    print('inside:')
    my_function()

# print('outside:')
# my_function()


@contextmanager
def context_logging(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

with context_logging(logging.DEBUG, 'my-log') as logger:
    logger.debug('this is my context_logging debug ')
    logging.debug('this will not print')

logger = logging.getLogger('my-log')
logger.debug('debug will not print')
logger.warning('warning will print')
logger.error('error will print')