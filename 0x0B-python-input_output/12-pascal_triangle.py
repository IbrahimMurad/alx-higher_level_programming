#!/usr/bin/python3
""" This module defines pascal_triangle function
"""


def pascal_triangle(n):
    """  returns a list of lists of integers representing
    the Pascal’s triangle of n
    """

    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        triangle.append([1])
        loop_len = len(triangle[i - 1]) - 1
        prev = triangle[i - 1]
        triangle[i].extend([prev[j] + prev[j + 1] for j in range(loop_len)])
        triangle[i].append(1)
    return triangle
