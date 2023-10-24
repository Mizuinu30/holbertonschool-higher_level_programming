#!/usr/bin/python3

# models/base.py

class Base:
    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id  # Assign id if provided
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  # Assign a new value to id
