#!/usr/bin/python3
"""defines a function to create an object from a JSON representation
from a file"""


def load_from_json_file(filename):
    """ Creates an object from a JSON representation from a file"""
    import json
    with open(filename, 'r') as f:
        return json.load(f)
