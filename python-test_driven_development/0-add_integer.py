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
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Perform the addition and return the result as an integer
    return int(a + b)
