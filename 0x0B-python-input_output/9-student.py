#!/usr/bin/python3
""" In this module, we define class Student,
that has class to JSON in it
"""


class Student:
    """
    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with <first_name>, <last_name>
    Public method def to_json(self):
        retrieves a dictionary representation of a Student instance
    """

    def __init__(self, first_name, last_name, age):
        """ Initializes <first_name>, <last_name> and age """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance """

        return self.__dict__
