#!/usr/bin/python3
""" In this module we define a function that
writes an Object to a text file, using a JSON representation
"""
dump = __import__('json').dump


def save_to_json_file(my_obj, filename):
    """  writes an Object to a text file,
    using a JSON representation
    """

    with open(filename, 'w', encoding="utf-8") as f:
        dump(my_obj, f)
