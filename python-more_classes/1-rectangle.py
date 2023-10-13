#!/usr/bin/python3
""" Insert module comment here """


class Rectangle:
    """ defines an empty class rectangle """

    def __init__(self, width=0, height=0):
        """ initializes the 'width' and 'height' attributes """
        self.width = width
        self.height = height

    @property
    def height(self):
        """retrieves the height attribute"""
        return self.__height

    @property
    def width(self):
        """retrieves the width attribute"""
        return self.__width

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("heigth must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("heigth must be >= 0")
        else:
            self.__width = value
