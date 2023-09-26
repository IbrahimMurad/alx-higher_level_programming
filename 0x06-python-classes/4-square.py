#!/usr/bin/python3

""" This module focuses on building a class with private instance attribute
 with certain condtions, raising esceptions if not satisfied. """


class Square:
    """ This class holds a size value. """

    def __init__(self, size=0):
        """ This initializes the size value. """

        self.size = size

    def area(self):
        """ Returns the area of the size. """
        return self.size * self.size

    @property
    def size(self):
        """ Returns the value 'size'. """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size to value. """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
