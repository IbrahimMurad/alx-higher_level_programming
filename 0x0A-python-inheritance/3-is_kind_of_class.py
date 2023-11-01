#!/usr/bin/python3
""" In this module we define a function that checks
if an object is an instance of a specific class or not
"""


def is_kind_of_class(obj, a_class):
    """  returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.
    """

    return isinstance(obj, a_class)
