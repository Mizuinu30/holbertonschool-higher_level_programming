#!/usr/bin/python3
"""This module contains a function that returns True if the object is an
instance of, or if the object is an instance of a class that inherited from,
the specified class; otherwise False."""


def inherits_from(obj, a_class):
    """checks if object is instance of a class that inherited from a_class

    Args:
        obj: object
        a_class: class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
