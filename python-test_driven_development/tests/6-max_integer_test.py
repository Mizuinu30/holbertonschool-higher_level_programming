#!/usr/bin/python3

    """ Module for testing max_integer in  list
    """

def max_integer(list=[]):
    """ Function that finds the max integer
    Args:
        list: list to find the max integer
    Returns:
        The max integer in the list
    Raises:
        TypeError: if list is not a list of integers
    """

    if len(list) == 0:
        return None
    max = list[0]
    i = 1
    while i < len(list):
        if list[i] > max:
            max = list[i]
        i += 1
    return max
