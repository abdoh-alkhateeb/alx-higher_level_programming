#!/usr/bin/python3
"""
Module that has the definition of print_square function.
"""


def print_square(size):
    """
    Function that prints a square with the character #.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
