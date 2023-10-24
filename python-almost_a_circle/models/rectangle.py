#!/usr/bin/python3
""" class Rectangle that inherits "Base"
Private instance Attributes, with it own
public getter and setter
    -__width -> width
    -__height -> height
    -__x -> x
    -__y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Class methods:
    super class with id
    assign each argument to the right attribute
Raises:
    TypeError: value must be an integer
    ValueError: value must be > 0
Public method def area(self): return area value of Rectangle
Public method def display(self): prints in stdout the Rectangle
Public method def update(self, *args):
    -1st argument: id attribute
    -2nd argument: width attribute
    -3rd argument: height attribute
    -4th argument: x attribute
    -5th argument: y attribute
    -"no-keyword arguments" Argument order is super important
"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init Method
        Args:
            -width (int)
            -height (int)
            -x (int)
            -y (int)
            -id (int)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
