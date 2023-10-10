#!/usr/bin/python3
""" In this module we define a function that reads a file
"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout
    """

    if filename == "":
        return
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
