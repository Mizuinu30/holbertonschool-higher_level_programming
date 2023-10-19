#!/usr/bin/python3
"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, other):
        """eq() method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ne() method"""
        return super().__eq__(other)
