#!/usr/bin/python3
"""
Module that defines Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class the defines Square logic.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Method that returns string representation of self.
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Getter for attribute size.
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for attribute size.
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Method that updates self with new attributes.
        """

        if args is not None and len(args) != 0:
            attributeMap = {0: "id", 1: "size", 2: "x", 3: "y"}

            for i in range(len(args)):
                self.__setattr__(attributeMap[i], args[i])
        else:
            for key in kwargs:
                self.__setattr__(key, kwargs[key])

    def to_dictionary(self):
        """
        Method that returns dictionary representation of self.
        """

        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
