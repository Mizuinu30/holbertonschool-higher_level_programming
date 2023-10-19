#!/usr/bin/python3
"""Module to create a class based on 7-base_geometry.py"""

Basegemetry = __import__('7-base_geometry').BaseGeometry


class Rectangle(Basegemetry):
    """
        rectangle taht inherits from BaseGeometry
    """
    def__init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
