""" 
This module defines a function that adds two integer
the two integers must be integers or floats
otherwise through TypeError exception
"""

def add_integer(a, b=98):
    """
    adds two integers
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
