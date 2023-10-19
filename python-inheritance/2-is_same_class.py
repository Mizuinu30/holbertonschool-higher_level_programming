#!/usr/bin/python3
"""returns True if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """_summary_

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_
    """
    if type(obj) is a_class:
        return True
    else:
        return False
