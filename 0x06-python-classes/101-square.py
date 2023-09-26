#!/usr/bin/python3

""" This module focuses on building a class with private instance attribute
 with certain condtions, raising esceptions if not satisfied. """


class Square:
    """ This class holds a size value. """

    def __init__(self, size=0, position=(0, 0)):
        """ This initializes the size value. """

        self.size = size
        self.position = position

    def area(self):
        """ Returns the area of the size. """
        return self.size * self.size

    def my_print(self):
        """ prints in stdout the square with the character #. """
        if self.size == 0:
            print()
        else:
            for y in range(self.position[1]):
                print()
            for i in range(self.size):
                for x in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()

    @property
    def size(self):
        """ Returns the value 'size'. """
        return self.__size

    @property
    def position(self):
        """ Returns the value 'size'. """
        return self.__position

    @size.setter
    def size(self, value):
        """ sets size to value. """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ sets size to value. """

        if is_valid_position(value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def __str__(self):
        """ This what makes this class printable. """

        str_to_print = ""
        if self.size == 0:
            return str_to_print
        for y in range(self.position[1]):
            str_to_print += "\n"
        for i in range(self.size):
            for x in range(self.position[0]):
                str_to_print += " "
            for j in range(self.size):
                str_to_print += "#"
            str_to_print += "\n"
        return str_to_print[:-1]


def is_valid_position(value):
    if type(value) is tuple:
        if len(value) == 2:
            if type(value[0]) is int and type(value[1]) is int:
                if value[0] >= 0 and value[1] >= 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
