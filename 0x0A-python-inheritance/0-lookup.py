#!/usr/bin/python3
"""
Module that defines lookup function.
"""


def lookup(obj):
    """
    Function that returns list of available attributes and methods of object.
    """

    return dir(obj)
