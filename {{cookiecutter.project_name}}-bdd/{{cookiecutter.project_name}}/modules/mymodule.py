"""
Module example.

You can use modules for simplify the functions calls in your tests.
"""
from logging import getLogger


logger = getLogger(__name__)


def add(x, y):
    logger.debug('Logging example')
    return x + y
