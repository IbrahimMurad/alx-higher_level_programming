#!/usr/bin/python3
""" In this module we define a function that checks
if an object is exactly an instance of a specific class or not
"""


def is_same_class(obj, a_class):
    """  returns True if the object is exactly an instance
    of the specified class; otherwise False.
    """

    if type(obj) is a_class:
        return True
    else:
        return False