"""
This module defines a function that prints a square with the character #
<size> is the side length of the square
<size> must be an integer or raise TypeError
if <size> is less than 0, raise a ValueError
if <size> is a float and is less than 0, raise a TypeError
"""


def print_square(size):
    """
    prints a square with #
    """

    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if type(size) is int and size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0.0:
        raise TypeError("size must be an integer")
    for i in range(int(size)):
        print("{}".format('#' * int(size)))
