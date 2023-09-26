#!/usr/bin/python3

""" This module defines a class names 'MagicClass' that holds
the radius of a circle, and calculates its area and its circumference """
math = __import__('math')


class MagicClass:
    """ This class gets the radius and
    calculates the area and the circumference. """

    def __init__(self, radius=0):
        """ Initializes the value of the radius. """

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Calculates the area. """

        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Calculates the circumference."""

        return 2 * math.pi * self.__radius
