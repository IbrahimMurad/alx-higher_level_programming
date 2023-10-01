#!/usr/bin/python3
"""
This module defines a function that takes a string as an input
and prints it with 2 new lines after each of
these characters: ., ? and :
<text> must be a string otherwise raise TypeError
There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """
    prints <text> with 2 newlines after ., ?, :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    temp_str = ""
    list_of_lines = []
    for c in text:
        if c not in ['.', ':', '?']:
            temp_str += c
        else:
            list_of_lines.append(temp_str.strip())
            list_of_lines[-1] += '\n'
            temp_str = ""
    if not len(temp_str) == 0:
        list_of_lines.append(temp_str.strip())
    for s in list_of_lines:
        print("{}".format(s))
