#!/usr/bin/python3
"""
Module that defines Square class.
"""


class Square:
    """
    Class that defines Square objects.
    """
    def __init__(self, size):
        """
        Method that constructs a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
