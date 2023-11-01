#!/usr/bin/python3
""" In this module we define a class that
inherits from BaseGeomerty class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ This class inherits from BaseGeometry
    has Instantiation function
    """

    def __init__(self, width, height):
        """ Intializes the width and height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
