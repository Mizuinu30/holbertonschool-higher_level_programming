#!/usr/bin/python3
# A function that prints all items in a list in reverse order
def print_reversed_list_integer(my_list=[]):
    # With these parameters, the loop iterates in reverse order, starting from the last element of the list and moving towards the first element, one step at a time.
    for i in range(len(my_list) - 1, -1, -1):
        print("{}".format(my_list[i]))
