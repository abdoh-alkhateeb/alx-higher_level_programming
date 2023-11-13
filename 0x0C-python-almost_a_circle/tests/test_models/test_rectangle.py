#!/usr/bin/python3
"""
Module that tests class Rectangle.
"""
import unittest
import unittest.mock
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def setUp(self):
        """
        Method called to prepare the test fixture.
        """

        Rectangle.__bases__[0]._Base__nb_objects = 0

    def tearDown(self):
        """
        Method called immediately after the test method has been called.
        """

        pass

    def test_constructor(self):
        """
        Test the constructor of the Rectangle class.
        """

        self.assertEqual(Rectangle(1, 1).id, 1)
        self.assertEqual(Rectangle(1, 1, 1, 1, 1488).id, 1488)

        with self.assertRaises(TypeError):
            Rectangle("x", 1)

        with self.assertRaises(TypeError):
            Rectangle(1, "x")

        with self.assertRaises(TypeError):
            Rectangle(1, 1, "x")

        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, "x")

        with self.assertRaises(ValueError):
            Rectangle(0, 1)

        with self.assertRaises(ValueError):
            Rectangle(1, 0)

        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)

        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)

    def test_width_setter(self):
        """
        Test the width setter of the Rectangle class.
        """

        rect = Rectangle(1, 1)
        rect.width = 5
        self.assertEqual(rect.width, 5)

        with self.assertRaises(TypeError):
            rect.width = "invalid"

        with self.assertRaises(ValueError):
            rect.width = 0

    def test_height_setter(self):
        """
        Test the height setter of the Rectangle class.
        """

        rect = Rectangle(1, 1)
        rect.height = 5
        self.assertEqual(rect.height, 5)

        with self.assertRaises(TypeError):
            rect.height = "invalid"

        with self.assertRaises(ValueError):
            rect.height = 0

    def test_x_setter(self):
        """
        Test the x setter of the Rectangle class.
        """

        rect = Rectangle(1, 1)
        rect.x = 5
        self.assertEqual(rect.x, 5)

        with self.assertRaises(TypeError):
            rect.x = "invalid"

        with self.assertRaises(ValueError):
            rect.x = -1

    def test_y_setter(self):
        """
        Test the y setter of the Rectangle class.
        """

        rect = Rectangle(1, 1)
        rect.y = 5
        self.assertEqual(rect.y, 5)

        with self.assertRaises(TypeError):
            rect.y = "invalid"

        with self.assertRaises(ValueError):
            rect.y = -1

    def test_area(self):
        """
        Test the area method of the Rectangle class.
        """

        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        """
        Test the display method of the Rectangle class.
        """

        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch("sys.stdout",
                                 new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """
        Test the str method of the Rectangle class.
        """

        rect = Rectangle(4, 5, 1, 2, 42)
        expected_str = "[Rectangle] (42) 1/2 - 4/5"
        self.assertEqual(str(rect), expected_str)

    def test_update(self):
        """
        Test the update method of the Rectangle class.
        """

        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(2, 3, 4, 5, 6)
        expected = {"id": 2, "width": 3, "height": 4, "x": 5, "y": 6}
        self.assertEqual(rect.to_dictionary(), expected)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method of the Rectangle class.
        """

        rect = Rectangle(7, 8, 9, 10, 11)
        expected = {"id": 11, "width": 7, "height": 8, "x": 9, "y": 10}
        self.assertEqual(rect.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
