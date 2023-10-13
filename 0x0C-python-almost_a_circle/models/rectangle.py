#!/usr/bin/python3
""" In this module, we define Rectangle class
that inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """ A clas that inherits from Base class
    that copycats a rectangle with height and width

    height: the height of the rectangle
    width: the width of the rectangle
    __x: the x position of the rectangle
    __y: the y position of the rectangle

    """

    @property
    def width(self):
        """ getter for <width> """

        return self.__width

    @width.setter
    def width(self, width):
        """ setter for width """

        if type(width) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if width <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = width

    @property
    def height(self):
        """ getter for <height> """

        return self.__height

    @height.setter
    def height(self, height):
        """ setter for height """

        if type(height) is not int:
            raise TypeError("{} must be an integer".format("height"))
        if height <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = height

    @property
    def x(self):
        """ getter for <x> """

        return self.__x

    @x.setter
    def x(self, x):
        """ setter for x """

        if type(x) is not int:
            raise TypeError("{} must be an integer".format("x"))
        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = x

    @property
    def y(self):
        """ getter for <y> """

        return self.__y

    @y.setter
    def y(self, y):
        """ setter for y """

        if type(y) is not int:
            raise TypeError("{} must be an integer".format("y"))
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes <width>, <height>, <x> and <y> """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ returns the area of the rectangle
        width x height
        """

        return self.width * self.height

    def display(self):
        """ draws the rectangle by # """

        print("\n" * self.y, end='')
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ prints [Rectangle] (<id>) <x>/<y> - <width>/<height>
        if a rectangle is passed to print
        """

        my_str = "[Rectangle] ({}) {}/".format(self.id, self.x)
        my_str += "{} - {}/{}".format(self.y, self.width, self.height)
        return my_str
