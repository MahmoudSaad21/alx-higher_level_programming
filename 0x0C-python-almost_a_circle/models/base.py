#!/usr/bin/python3
"""
    contains a class Base.
"""
import json
import csv


class Base:
    """base class for the entire project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
           Initializes the class attributes.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
