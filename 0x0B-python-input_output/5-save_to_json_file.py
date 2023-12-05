#!/usr/bin/python3
"""
    5-save_to_json_file: save_to_json_file()
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON rep."""
    with open(filename, "w") as files:
        json.dump(my_obj, files)
