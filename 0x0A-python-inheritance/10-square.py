#!/usr/bin/python3
""" In this module we define a class that
inherits from Rectangle class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ This class inherits from Rectangle
    has Instantiation function
    implement area
    """

    def __init__(self, size):
        """ Intializes the size of the square
        """

        super().__init__(size, size)

    def area(self):
        """ returns the area of the square (size x size)
        """

        return super().area()
