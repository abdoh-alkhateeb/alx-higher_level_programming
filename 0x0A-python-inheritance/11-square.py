#!/usr/bin/python3
"""
Module that defines Square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that defines Square.
    """

    def __init__(self, size):
        """
        Method that constructs Square.
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Method that calculates area.
        """

        return self.__size ** 2

    def __str__(self):
        """
        Method that returns string representation.
        """

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
