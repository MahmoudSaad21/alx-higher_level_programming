#!/usr/bin/python3
for num in range(100):
    if num != 99:
        print('{:0>2d}, '.format(num), end="")
    else:
        print('{}'.format(num))
