#!/usr/bin/python3
"""
Module defining LockedClass.
"""


class LockedClass:
    """
    A locked class  that prevents the user from dynamically
    creating new instance attributes, except if the new instance
    attribute is called first_name.
    """

    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        self.first_name = first_name
