#!/usr/bin/python3
"""
Module that defines Base class.
"""
import json


class Base:
    """
    Class the defines Base logic.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method that returns JSON string representation of its argument.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method that writes JSON string representation of its arg to a file.
        """

        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Method that returns list of dicts from its JSON string argument.
        """

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Method that returns an instance with all attributes already set.
        """

        dummy = cls(1, 1)
        dummy.x = 0
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Method that returns a list of instances.
        """

        try:
            with open(cls.__name__ + ".json", "r") as f:
                instances = cls.from_json_string(f.read())

            for i in range(len(instances)):
                instances[i] = cls.create(**instances[i])

            return instances
        except FileNotFoundError:
            return []
