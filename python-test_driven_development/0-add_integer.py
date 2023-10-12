#!/usr/bin/python3
"""
    module that adds 2 integers
"""


def add_integer(a, b=98):
    """ add two integers or floats
    >>> add_integer = __import__('0-add_integer').add_integer
    >>> add_integer(3, 5)
    8
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> (add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last): ...
    >>> add_integer(None)
    Traceback (most recent call last): ...
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
