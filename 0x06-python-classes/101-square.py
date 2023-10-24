#!/usr/bin/python3
"""
Module that defines Square class.
"""


class Square:
    """
    Class that defines Square objects.
    """
    def __init__(self, size=0, pos=(0, 0)):
        """
        Method that constructs a new Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not (isinstance(pos, tuple) and len(pos) == 2 and
                isinstance(pos[0], int) and isinstance(pos[1], int) and
                pos[0] >= 0 and pos[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = pos

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

    @property
    def position(self):
        """
        Getter for position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position attribute.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Method that calculates Square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method that prints the Square to stdin with # character
        """
        if self.__size == 0:
            print("")
        else:
            print('\n' * self.__position[1], end="")
            for i in range(self.__size):
                print((' ' * self.__position[0]) + ('#' * self.__size))

    def __str__(self):
        """
        Method that returns the Square string representation.
        """
        result = ""
        if self.__size != 0:
            result += '\n' * self.__position[1]
            for i in range(self.__size):
                result += ' ' * self.__position[0] + '#' * self.__size + '\n'

        return result.rstrip()
