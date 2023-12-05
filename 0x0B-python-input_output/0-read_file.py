#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as files:
        for line in files:
            print(line, end="")
    files.closed
