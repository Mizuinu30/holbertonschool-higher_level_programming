#!/usr/bin/python3
""" defines a function that counts the number of lines of a text file"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    count = 0
    with open(filename) as f:
        while f.readline() is not "":
            count += 1
    return count
