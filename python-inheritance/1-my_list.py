#!/usr/bin/python3
""" Mylist Class
    Module that defines a class Mylist that inherits from list"""


class MyList(list):
    """class that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
