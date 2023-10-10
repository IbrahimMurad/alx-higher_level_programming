#!/usr/bin/python3
""" In this module we define a class BaseGeometry
that has a public instance that raises an exception
and a public instance that validates a value
"""


class BaseGeometry:
    """ a class that do nothing except for
    a public instance that raises an exception
    and a public instance that validates a value
    """

    def area(self):
        """ raises an exception that prints a message
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value
        if value is not an integer: raise a TypeError exception
        if value is less or equal to 0: raise a ValueError exception
        """
        
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
