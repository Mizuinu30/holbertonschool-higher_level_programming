#!/usr/bin/python3
""" defines a function that writes a string to a text file
(UTF8) and returns the number of characters writen"""


def write_file(filename="", text=""):
    """writes strings to text file"""
    with open(filename, 'w') as f:
        return f.write(text)
