#!/usr/bin/python3
# A function that prints all items in a list in reverse order
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    # With these parameters, the loop iterates in reverse order.
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
