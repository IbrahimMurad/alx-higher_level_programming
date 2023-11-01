#!/usr/bin/python3
""" In this module we define a class that inhirates from class list
"""


class MyList(list):
    """ This class inhirates from list
    and defines a method that prints the list sorted
    """

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)
        """

        print(sorted(self))
