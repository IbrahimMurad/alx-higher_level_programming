#!/usr/bin/python3
""" This module defines a class named Rectangle
that has width and height and can get the area and the perimeter
of a rectangle with same width and height
Also, it can print a rectangle of print_symbol
and can be recreated using string representation
handles the destractors
has instance counter
can compare two rectangles
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
    print() and str() can print the rectangle with the character #
    repr() returns the string used to recreate a new instance using eval()
    print somethning when deleted
    Public class attribute <number_of_instances>
    Public class attribute <print_symbol>
    Static method def <bigger_or_equal> that
          returns the biggest rectangle based on the area
    """

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ returns the string that would be printed
        if passed to print()
        """

        my_str = ""
        if self.width == 0 or self.height == 0:
            return my_str
        row_str = ""
        for i in range(self.width):
            row_str += str(self.print_symbol)
        row_str += '\n'
        for i in range(self.height):
            my_str += row_str
        return my_str[:-1]

    def __repr__(self):
        """ return a string representation of the rectangle
        to be able to recreate a new instance
        """

        return "Rectangle(" + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        """ prints a message when deleting an instance
        and decreamenting number_of_instance by 1 """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """

        if not type(rect_1) is Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not type(rect_2) is Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
