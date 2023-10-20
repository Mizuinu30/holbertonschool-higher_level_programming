#!/usr/bin/python3
import sys
import json
""" defines a function that adds all arguments to a Python list
and then save them to a file"""


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


# Check if the add_item.json file exists and load its content
try:
    items = load_from_json_file('add_item.json')
except FileNotFoundError:
    items = []

# Add command-line arguments to the items list
for arg in sys.argv[1:]:
    items.append(arg)

# Save the updated items list to add_item.json
save_to_json_file(items, 'add_item.json')
