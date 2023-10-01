"""
This module defines a function that divides all elements of a matrix by number
the matrix must be list of lists and the number is int or float
all new elements are rounded to 2 decimal places
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix by a number
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not len(list(dict.fromkeys([len(row) for row in matrix]))) == 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mat = [[round(i / div, 2) for i in row] for row in matrix]
    return new_mat
