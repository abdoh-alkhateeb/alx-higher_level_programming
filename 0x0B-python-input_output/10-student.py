#!/usr/bin/python3
"""
Module that defines Student class.
"""


class Student:
    """
    Class that represents Student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Constructor for Student class.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method that returns dict that contains info the object.
        """

        if attrs is None:
            return self.__dict__

        return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
