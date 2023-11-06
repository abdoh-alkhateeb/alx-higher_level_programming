#!/usr/bin/python3
"""
Module that defines Rectangle class.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that defines Rectangle.
    """

    def __init__(self, width, height):
        """
        Method that constructs Rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
