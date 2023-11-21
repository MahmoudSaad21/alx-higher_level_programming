#!/usr/bin/python3
"""a class Square that defines a square by:(based on 2-square.py)"""


class Square:
    """This is a class with an init method"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Returns the current square area """
        return (self.__size**2)
