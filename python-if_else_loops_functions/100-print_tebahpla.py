#!/usr/bin/python3
def print_tebalhpla():
    for char_code in range(ord("z"), ord("A") - 1, -1):
        char = chr(char_code)
        print(char, end="")
