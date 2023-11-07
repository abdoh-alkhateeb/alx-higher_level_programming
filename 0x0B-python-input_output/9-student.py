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

    def to_json(self):
        """
        Method that returns dict that contains info the object.
        """

        return self.__dict__
