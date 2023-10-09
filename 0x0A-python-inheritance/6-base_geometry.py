#!/usr/bin/python3
""" In this module we define a class BaseGeometry
that has a public instance that raises an exception
"""


class BaseGeometry:
    """ a class that do nothing except for
    a public instance that raises an exception
    """

    def area(self):
        """ raises an exception that prints a message
        """

        raise Exception("area() is not implemented")
