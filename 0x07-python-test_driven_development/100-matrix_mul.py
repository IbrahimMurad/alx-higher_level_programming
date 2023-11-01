#!/usr/bin/python3
""" This module multiplies two matrices
each matrix must be a non-empty matrix
its elements must be integers or floats
And of course, first matrix's columns must equal
the second matrix's rows.
"""


def matrix_mul(m_a, m_b):
    """ multiplies 2 matrices
    if m_a or m_b is not a list: raise a TypeError
    if m_a or m_b is not a list of lists: raise a TypeError
    if m_a or m_b is empty (it means: = [] or = [[]]): raise a ValueError
    if one element of those matrices is not int or float raise a TypeError
    if m_a or m_b is not a rectangle raise a TypeError
    If m_a and m_b cant be multiplied: raise a ValueError
    """

    # check if both mats are lists
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    # checks if both mats are lists of lists
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    # checks if the tow mats are non-empty
    if len(m_a) == 0:
        raise TypeError("m_a can't be empty")
    if len(m_a[0]) == 0:
        raise TypeError("m_a can't be empty")
    if len(m_b) == 0:
        raise TypeError("m_b can't be empty")
    if len(m_b[0]) == 0:
        raise TypeError("m_b can't be empty")

    # checks if the two mats contain only integers and floats
    for row in m_a:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    # checks if the two mats are rectangles
    if not len(list(dict.fromkeys([len(row) for row in m_a]))) == 1:
        raise TypeError("each row of m_a must be of the same size")
    if not len(list(dict.fromkeys([len(row) for row in m_b]))) == 1:
        raise TypeError("each row of m_b must be of the same size")

    # checks if the two mats can be multiplied
    # (number of m_a columns = number of m_b rows)
    if not len(m_a[0]) == len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # implementing the function
    result = []
    for row in m_a:
        res_row = []
        for i in range(len(m_b[0])):
            element = 0
            for j in range(len(row)):
                element += row[j] * m_b[j][i]
            res_row.append(element)
        result.append(res_row)
    return result
