#!/usr/bin/python3
"""derines a function to write a JSON representation of an object
to a text file"""


def save_to_json_file(my_obj, filename):
    """writes a JSON representation of an object to a text file"""
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj, ensure_ascii=False))
