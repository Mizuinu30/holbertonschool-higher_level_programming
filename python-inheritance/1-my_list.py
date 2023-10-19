#!/usr/bin/python3
"""
    Module that defines a class Mylist that inherits from list
"""


class MyList(list):
    """class that inherits from list"""

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        list_sorted = []
        for num in self:
            list_sorted.append(num)
        list_sorted.sort()
        print(list_sorted)
