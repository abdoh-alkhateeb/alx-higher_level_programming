#!/usr/bin/python3
"""
Module that defines Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Class the defines Rectangle logic.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for attribute width.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for attribute width.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter for attribute height.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for attribute height.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Getter for attribute x.
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for attribute x.
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Getter for attribute y.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for attribute y.
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Method that calculates area of self.
        """

        return self.__width * self.__height

    def display(self):
        """
        Method that prints self in stdout.
        """

        print("\n" * self.__y, end="")

        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Method that returns string representation of self.
        """

        string = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        string += f" - {self.__width}/{self.__height}"

        return string

    def update(self, *args, **kwargs):
        """
        Method that updates self with new attributes.
        """

        if args is not None and len(args) != 0:
            attributeMap = {0: "id", 1: "width", 2: "height", 3: "x", 4: "y"}

            for i in range(len(args)):
                self.__setattr__(attributeMap[i], args[i])
        else:
            for key in kwargs:
                self.__setattr__(key, kwargs[key])

    def to_dictionary(self):
        """
        Method that returns dictionary representation of self.
        """

        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
