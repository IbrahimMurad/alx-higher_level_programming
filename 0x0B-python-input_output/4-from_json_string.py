#!/usr/bin/python3
""" In this module we define a function that
 returns an object represented by a JSON string
"""
loads = __import__('json').loads


def from_json_string(my_str):
    """   returns an object (Python data structure)
    represented by a JSON string:
    """

    return loads(my_str)
