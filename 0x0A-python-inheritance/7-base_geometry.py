#!/usr/bin/python3
"""
Module that defines BaseGeometry class.
"""


class BaseGeometry:
    """
    Class that defines BaseGeometry.
    """

    def area(self):
        """
        Method that calculates area.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates an integer.
        """

        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
