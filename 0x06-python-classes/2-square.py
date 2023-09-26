#!/usr/bin/python3

""" This module focuses on building a class with private instance attribute
 with certain condtions, raising esceptions if not satisfied. """


class Square:
    """ This class holds a size value. """

    def __init__(self, size=0):
        """ This initializes the size value. """

        try:
            if type(size) is not int:
                raise TypeError
            elif size < 0:
                raise ValueError
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
