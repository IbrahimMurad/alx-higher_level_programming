#!/usr/bin/python3
""" In this module, we define Base class
that has a private attribute and a constructor
"""


class Base:
    """ This class will be the “base”
    of all other classes in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes id """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
