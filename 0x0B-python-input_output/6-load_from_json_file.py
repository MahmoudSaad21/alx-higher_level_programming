#!/usr/bin/python3
"""
    6-load_from_json_file: load_from_json_file()
"""


import json


def load_from_json_file(filename):
    """loads an object to from JSON file."""
    with open(filename, "r") as j_file:
        return json.load(j_file)
