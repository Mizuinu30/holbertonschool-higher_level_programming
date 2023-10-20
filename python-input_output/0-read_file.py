#!/usr/bin/python3
""" defines a function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """ reads a text file and prints it to stdout"""
    with open(filename) as f:
        print(f.read(), end="")
