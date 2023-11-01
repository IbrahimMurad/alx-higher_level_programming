#!/usr/bin/python3
""" In this module we define a function that appends to a file
"""


def append_write(filename="", text=""):
    """ appends a string to a text file (UTF8)
    and returns the number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
