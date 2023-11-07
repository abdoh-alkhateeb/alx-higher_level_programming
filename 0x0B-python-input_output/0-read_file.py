#!/usr/bin/python3
"""
Module that defines read_file function.
"""


def read_file(filename=""):
    """
    Function that reads a files and prints its content to stdin.
    """

    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
