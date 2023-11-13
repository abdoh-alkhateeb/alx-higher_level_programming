#!/usr/bin/python3
"""
Module that tests class Square.
"""
import unittest
import unittest.mock
import io
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def setUp(self):
        """
        Method called to prepare the test fixture.
        """

        Square.__mro__[2]._Base__nb_objects = 0

    def tearDown(self):
        """
        Method called immediately after the test method has been called.
        """

        pass

    def test_constructor(self):
        """
        Test the constructor of the Square class.
        """

        self.assertEqual(Square(1).id, 1)
        self.assertEqual(Square(1, 1, 1, 1488).id, 1488)

        with self.assertRaises(TypeError):
            Square("x")

        with self.assertRaises(TypeError):
            Square(1, "x")

        with self.assertRaises(TypeError):
            Square(1, 1, "x")

        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(ValueError):
            Square(1, -1)

        with self.assertRaises(ValueError):
            Square(1, 1, -1)

    def test_size_setter(self):
        """
        Test the size setter of the Square class.
        """

        square = Square(3)
        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

        with self.assertRaises(TypeError):
            square.size = "invalid"

        with self.assertRaises(ValueError):
            square.size = 0

    def test_str(self):
        """
        Test the str method of the Square class.
        """
        square = Square(4, 2, 3, 42)
        expected_str = "[Square] (42) 2/3 - 4"
        self.assertEqual(str(square), expected_str)

    def test_update(self):
        """
        Test the update method of the Square class.
        """

        square = Square(1, 1, 1, 1)
        square.update(2, 3, 4, 5)
        expected = {'id': 2, 'size': 3, 'x': 4, 'y': 5}
        self.assertEqual(square.to_dictionary(), expected)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method of the Square class.
        """

        square = Square(5, 2, 3, 42)
        expected = {'id': 42, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected)


if __name__ == '__main__':
    unittest.main()
