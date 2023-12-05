#!/usr/bin/python3
"""This module adds all arguments to a Python list and save them to a file."""


import sys

if __name__ == "__main__":
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        itemes = load("add_item.json")
    except FileNotFoundError:
        itemes = []
    itemes.extend(sys.argv[1:])
    save(itemes, "add_item.json")
