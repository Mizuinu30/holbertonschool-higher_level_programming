#!/usr/bin/python3
""" Mylist Class
    Module that defines a class Mylist that inherits from list"""


class MyList(list):
    """class that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        list_sorted = []
        for i in self:
            list_sorted.append(i)
        list_sorted.sort()
        print(list_sorted)
