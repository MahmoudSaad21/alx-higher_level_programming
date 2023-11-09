#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Use list comprehension to create a new dictionary with unwanted keys removed
    return {k: v for k, v in a_dictionary.items() if v != value}
