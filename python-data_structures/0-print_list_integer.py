#!/usr/bin/python3
# A function that prints all integer of a list

def print_list_integer(my_list):
    for item in my_list:
        print("{:d}".format(my_list[item - 1]))
