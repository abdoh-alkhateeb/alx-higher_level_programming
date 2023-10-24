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

    def __eq__(self, other):
        """
        Overloads equal operator.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Overloads not equal operator.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Overloads greater than operator.
        """
        return self.area() > other.area()

    def __lt__(self, other):
        """
        Overloads less than operator.
        """
        return self.area() < other.area()

    def __ge__(self, other):
        """
        Overloads greater than or equal operator.
        """
        return self.area() >= other.area()

    def __le__(self, other):
        """
        Overloads less than or equal operator.
        """
        return self.area() <= other.area()
