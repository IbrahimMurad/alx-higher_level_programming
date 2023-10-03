#!/usr/bin/python3
""" This module defines a class that has no attributes
and prevents any creation of attributes except for 'first_name'
"""


class LockedClass:
    """ a class that has only one job, to prevent creating any extra
    attributes but 'first_name'
    """

    __slots__ = ['first_name']
