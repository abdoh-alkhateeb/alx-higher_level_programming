#!/usr/bin/python3
"""
Module that defines append_write function.
"""


def append_write(filename="", text=""):
    """
    Function that writes string at end of file and returns # of chars written.
    """

    with open(filename, "a", encoding="UTF-8") as f:
        bytes_written = f.write(text)

    return bytes_written
