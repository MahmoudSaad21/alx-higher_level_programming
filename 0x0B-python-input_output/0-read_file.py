#!/usr/bin/python3
"""
    0-read_file: read_file()
"""



def read_file(filename=""):
    """read_file reads text file and prints it"""
    with open(filename, 'r') as files:
        for line in files:
            print(line, end="")
    files.closed
