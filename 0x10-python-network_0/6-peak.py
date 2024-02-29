#!/usr/bin/python3
"""In this module, we define find_peak function
that returns the peak inside a list"""


def find_peak(my_list=list):
    """ returns the peak value in my_list """

    if len(my_list) == 0:
        return None
    else:
        return sorted(my_list)[-1]
