#!/usr/bin/python3
""" In this module we define a function that
checks if an object is an instance of a class that
is inherited from another class of not
"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.
    """

    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
