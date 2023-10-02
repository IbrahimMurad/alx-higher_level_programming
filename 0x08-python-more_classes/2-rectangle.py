#!/usr/bin/python3
""" This module defines a class named Rectangle
that has width and height and can get the area
of a rectangle with same width and height
"""


class Rectangle:
    """ a clss that holds informations of a rectangle
    private instance attribute <width>
    private instance attribute <height>
    getter for <width> and getter for <height>
    setter for <width> and setter for <height>
    <width> and <height> must be an integers, otherwise raise a TypeError
    if <width> or <height> is less than 0, raise a ValueError
    Public instance method <area> that returns the rectangle area
    Public instance method <perimeter> that returns the rectangle perimeter
    """

    @property
    def width(self):
        """ returns <width> """

        return self.__width

    @width.setter
    def width(self, value):
        """ sets <width> to <value> """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ returns <height> """

        return self.__height

    @height.setter
    def height(self, value):
        """ sets <height> to <value> """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """ Initializes both width and height """

        self.width = width
        self.height = height

    def area(self):
        """ returns the area of the rectangle """

        return self.width * self.height

    def perimeter(self):
        """ returns the perimeter of the rectangle
        if width or height is zero return 0
        """

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
