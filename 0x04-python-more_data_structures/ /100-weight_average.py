#!/usr/bin/python3
# weight_average - returns the weighted average of all intergers tuple.
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    return sum([mul(x[0], x[1]) for x in my_list]) / sum(x[1] for x in my_list)

# mul - returns x*y.
def mul(x, y):
    return x * y
