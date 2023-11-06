#!/usr/bin/python3
"""
Module that defines MyList class.
"""


class MyList(list):
    """
    Class that defines a special kind of list.
    """

    def print_sorted(self):
        """
        Function that prints list sorted.
        """

        print(sorted(self))
