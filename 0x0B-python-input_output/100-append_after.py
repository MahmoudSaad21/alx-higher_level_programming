#!/usr/bin/python3
"""This module defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file"""
    new_text = ""
    with open(filename) as r:
        for line in r:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, "w") as w:
        w.write(new_text)
