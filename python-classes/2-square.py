#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """Initialize the square with a given size.

        Args:
        - size: The size of the square's sides.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
