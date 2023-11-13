#!/usr/bin/python3
"""
Module that tests class Base.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """
    Class that tests class Base.
    """

    def setUp(self):
        """
        Method called to prepare the test fixture.
        """

        Base._Base__nb_objects = 0

        json_files = os.listdir(".")
        for file in json_files:
            if file.endswith(".json"):
                os.remove(file)

    def tearDown(self):
        """
        Method called immediately after the test method has been called.
        """

        pass

    def test_attributes(self):
        """
        Method that tests attributes of Base.
        """

        # Test whether __nb_objects exists or not.
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

        # Test default value of __nb_objects.
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

        # Test whether id exists or not.
        self.assertTrue(hasattr(Base(), "id"))

    def test_constructor(self):
        """
        Method that tests constructor of Base.
        """

        # Test when id provided is None.
        self.assertEqual(Base().id, 1)

        # Test autoincrement of id.
        self.assertEqual(Base().id, 2)

        # Test when id provided is not None.
        self.assertEqual(Base(12).id, 12)

        # Test autoincrement of id.
        self.assertEqual(Base().id, 3)

    def test_to_json_string(self):
        """
        Method that tests method to_json_string of Base.
        """

        # Test when list_dictionaries is None.
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

        # Test when list_dictionaries is an empty list.
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

        # Test when list_dictionaries has some data.
        data = [{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]
        result = Base.to_json_string(data)
        expected = '[{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]'
        self.assertEqual(result, expected)

    def test_save_to_file(self):
        """
        Method that tests method save_to_file of Base.
        """

        # Test when list_objs is None.
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            result = f.read()
            self.assertEqual(result, "[]")

        # Test when list_objs has some instances.
        class Dummy:
            def to_dictionary(self):
                return {"id": 1, "name": "dummy"}

        instances = [Dummy(), Dummy()]
        Base.save_to_file(instances)
        with open("Base.json", "r") as f:
            result = f.read()
            exp = '[{"id": 1, "name": "dummy"}, {"id": 1, "name": "dummy"}]'
            self.assertEqual(result, exp)

    def test_from_json_string(self):
        """
        Method that tests method from_json_string of Base.
        """

        # Test when json_string is None.
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

        # Test when json_string is an empty string.
        result = Base.from_json_string("")
        self.assertEqual(result, [])

        # Test when json_string has some data.
        json_string = '[{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]'
        result = Base.from_json_string(json_string)
        expected = [{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]
        self.assertEqual(result, expected)

    def test_create(self):
        """
        Method that tests method create of Base.
        """

        # Test creating an instance with dictionary data.
        dictionary = {"id": 8814, "width": 1488}
        result = Rectangle.create(**dictionary)
        self.assertEqual(result.id, 8814)
        self.assertEqual(result.width, 1488)

    def test_load_from_file(self):
        """
        Method that tests method load_from_file of Base.
        """

        # Test loading instances from a file that doesn't exist.
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

        # Test loading instances from a file with data.
        with open("Rectangle.json", "w") as f:
            f.write('[{"id": 88, "width": 8814}, {"id": 14, "height": 1488}]')

        result = Rectangle.load_from_file()

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)

        self.assertIsInstance(result[0], Rectangle)
        self.assertIsInstance(result[1], Rectangle)

        self.assertEqual(result[0].id, 88)
        self.assertEqual(result[0].width, 8814)

        self.assertEqual(result[1].id, 14)
        self.assertEqual(result[1].height, 1488)


if __name__ == "__main__":
    unittest.main()
