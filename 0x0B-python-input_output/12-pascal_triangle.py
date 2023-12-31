#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """returns a list of lists of integers"""
    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for j in range(n):
        for i in range(j - 1):
            rows[j][i + 1] = sum(rows[j - 1][i:i + 2])
    return rows
