#!/usr/bin/python3
""" In this module we define a function that
represent a string in JSON
"""
dumps = __import__('json').dumps


def to_json_string(my_obj):
    """  returns the JSON representation of an object (string)
    """

    return dumps(my_obj)
