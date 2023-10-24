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
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Getter for size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size attribute.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Method that calculates Square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method that prints the Square to stdin with # character
        """
        for i in range(self.__size):
            print('#' * self.__size)
        if self.__size == 0:
            print()
