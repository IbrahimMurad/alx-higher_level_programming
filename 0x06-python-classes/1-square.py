#!/usr/bin/python3

""" This is a demonistration of how to make a class.
 and declare a private instance attribute in it. """


class Square:
    """ This class has a private instance attribute. """
    def __init__(self, size):
        """ This initializes the size of the square to the passed value."""
        self.__size = size
