#!/usr/bin/python3
"""
Module that defines Rectangle class.
"""


class Rectangle:
    """
    Class that defines Rectangle object.
    """

    def __init__(self, width=0, height=0):
        """
        Constructor for Rectangle class.
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height

    @property
    def width(self):
        """
        Getter for width attribute.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        height for width attribute.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Returns area.
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Returns perimeter.
        """

        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Returns string representation.
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join(["#" * self.__width for i in range(self.__height)])

    def __repr__(self):
        """
        Returns eval-compatible string representation.
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
