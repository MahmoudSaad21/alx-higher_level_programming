#!/usr/bin/python3
def search_replace(my_list, search, replace):
    New_list = my_list.copy()
    i = 0
    for x in my_list:
        if x is search:
            New_list[i] = replace
        i += 1
    return (New_list)