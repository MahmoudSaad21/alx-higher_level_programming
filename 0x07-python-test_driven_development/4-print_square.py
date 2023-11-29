#!/usr/bin/python3
""" print_square prints a square depending on the "size" parameter"""


def print_square(size):
    """ Prints a square with a size"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return None

    for row in range(size):
        print('#' * size)
