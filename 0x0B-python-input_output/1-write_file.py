#!/usr/bin/python3
"""
Module that defines write_file function.
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to text file and returns # of chars written.
    """

    with open(filename, "w", encoding="UTF-8") as f:
        bytes_written = f.write(text)

    return bytes_written
