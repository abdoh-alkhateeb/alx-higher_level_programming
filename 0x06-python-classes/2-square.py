#!/usr/bin/python3
"""
Module that defines Square class.
"""


class Square:
    """
    Class that defines Square objects.
    """
    def __init__(self, size=0):
        """
        Method that constructs a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
