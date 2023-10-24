#!/usr/bin/python3
"""Module that defines MagicClass"""


import math


class MagicClass:
    """Class that defines MagicClass"""
    def __init__(self, radius=0):
        """Method that constructs MagicClass object"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Method that returns area of MagicClass object"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Method that returns circumference of MagicClass object"""
        return 2 * math.pi * self.__radius
