#!/usr/bin/python3

""" This module defines a class names 'MagicClass' that holds
the radius of a circle, and calculates its area and its circumference """


class MagicClass:
    """ This class gets the radius and
    calculates the area and the circumference. """

    def __init__(self, radius=0):
        """ Initializes the value of teh radius. """

        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """ Calculates the area. """

        return __import__('math').pi.pi * (self.__radius ** 2)

    def circumference(self):
        """ Calculates the circumference."""

        return 2 * __import__('math').pi * self.__radius
