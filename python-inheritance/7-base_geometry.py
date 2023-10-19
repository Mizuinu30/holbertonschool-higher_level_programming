#!/usr/bin/python3
"""Module to create a class based on 6-base_geometry.py"""


class BaseGeometry:

    def area(self):
        """
        Method that raises an exception
        """

    raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates value
        """
        if value is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
