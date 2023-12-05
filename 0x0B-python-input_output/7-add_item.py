#!/usr/bin/python3
"""
    This is a python script that adds all arguments to a Python List.
    List is then saved to a file.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":

    name = "add_item.json"

    try:
        a_list = load_from_json_file(name)
    except:
        a_list = []

    for arg in sys.argv[1:]:
        _list.append(arg)
    save_to_json_file(a_list, name)
