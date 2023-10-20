#!/usr/bin/python3
""" defines a function that returns the JSON
representation of an object (string)"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    import json
    return json.dumps(my_obj, ensure_ascii=False)
