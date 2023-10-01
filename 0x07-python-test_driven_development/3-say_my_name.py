"""
This module defines a function that prints
my name is 'first_name' 'last_name'
first_name and last_name must be strings
"""


def say_my_name(first_name, last_name=""):
    """
    prints 'my name is <first_name> <last_name>'
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))