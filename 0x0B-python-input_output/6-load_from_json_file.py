#!/usr/bin/python3
""" In this module we define a function that
reads an Object creates an Object from a “JSON file”
"""
load = __import__('json').load


def load_from_json_file(filename):
    """  creates an Object from a “JSON file”
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return load(f)
