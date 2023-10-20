#!/usr/bin/python3
""" defines a functionthat appends a string  to a text file"""


def append_write(filename="", text=""):
    """appends strings to text file"""
    with open(filename, 'a') as f:
        return f.write(text)
