#!/usr/bin/python3
# uniq_add - adds all unique integers in a list
def uniq_add(my_list=[]):
    unique = list(set(my_list))
    sum = 0
    for i in unique:
        sum += i
    return sum
