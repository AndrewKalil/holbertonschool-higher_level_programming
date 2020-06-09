#!/usr/bin/python3
"""Base unitests"""
from models.square import Square
from io import StringIO
import unittest
import sys


class BaseTest(unittest.TestCase):
    """tests for base class"""

    def test_init(self):
        """checking instantiation method"""
        test1 = Square(3)
        self.assertEqual(test1.size, 3)
        self.assertEqual(test1.x, 0)
        self.assertEqual(test1.y, 0)

        test2 = Square(2, 3, 1, 11)
        self.assertEqual(test2.size, 2)
        self.assertEqual(test2.x, 3)
        self.assertEqual(test2.y, 1)
        self.assertEqual(test2.id, 11)

        test3 = Square(5, 2)
        self.assertEqual(test3.size, 5)
        self.assertEqual(test3.x, 2)
        self.assertEqual(test3.y, 0)

    def test_possible_TypeError_rasies(self):
        """ensures all possible raises are covered for creating a rectangle"""
        with self.assertRaises(TypeError):
            Square("3")

        with self.assertRaises(TypeError):
            Square(5, "1", 5)

        with self.assertRaises(TypeError):
            Square(5, 1, "5")

    def possible_update_TypeErrors(self):
        """checking value erros when updating"""
        test = Square(1)
        with self.assertRaises(TypeError):
            test.update("3")

        with self.assertRaises(TypeError):
            test.update(1, 5, "1", 5)

        with self.assertRaises(TypeError):
            test.update(1, "5", 1, 5)

    def test_possible_ValueError_rasies(self):
        """ensures all possible raises are covered for creating a rectangle"""
        with self.assertRaises(ValueError):
            Square(-5)

        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(ValueError):
            Square(5, -1, 5)

        with self.assertRaises(ValueError):
            Square(5, 1, -5)

    def possible_update_VaueErrors(self):
        """checking type errors when updating"""
        test = Square(1)
        with self.assertRaises(ValueError):
            test.update(1, -4)

        with self.assertRaises(ValueError):
            test.update(height=-4)

        with self.assertRaises(ValueError):
            test.update(width=-3)

        with self.assertRaises(ValueError):
            test.update(1, 5, -1, 5)

        with self.assertRaises(ValueError):
            test.update(x=-1)

        with self.assertRaises(ValueError):
            test.update(1, 5, 1, -5)

        with self.assertRaises(ValueError):
            test.update(y=-5)

    def test_area(self):
        """testing the area for the rectangle method"""
        test1 = Square(4)
        self.assertEqual(test1.area(), 16)

        test2 = Square(5, 25, 45, 100)
        self.assertEqual(test2.area(), 25)

    def test_display(self):
        """testing the display printed to the stdout"""
        output = StringIO()
        sys.stdout = output
        test1 = Square(2)
        test1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            output.getvalue(), "##\n##\n")

    def test_display_with_shift(self):
        """testing the display printed to the stdout"""
        output = StringIO()
        sys.stdout = output

        test2 = Square(2, 3, 1)
        test2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            output.getvalue(), "\n   ##\n   ##\n")

    def test_str_for_square(self):
        """testing the string to be printed from __str__"""
        test1 = Square(3, 3, 2, 10)
        self.assertEqual(test1.__str__(), "[Square] (10) 3/2 - 3")

    def test_update_args_and_kwargs(self):
        """testing if update actually updates an object"""
        test1 = Square(3, 3, 2, 10)
        self.assertEqual(test1.__str__(), "[Square] (10) 3/2 - 3")
        test1.update(69)
        self.assertEqual(test1.__str__(), "[Square] (69) 3/2 - 3")
        test1.update(69, 6)
        self.assertEqual(test1.__str__(), "[Square] (69) 3/2 - 6")
        test1.update(69, 6, 9)
        self.assertEqual(test1.__str__(), "[Square] (69) 9/2 - 6")
        test1.update(69, 6, 9, 6)
        self.assertEqual(test1.__str__(), "[Square] (69) 9/6 - 6")
        test1.update(69, 6, 9, 6, 9)
        self.assertEqual(test1.__str__(), "[Square] (69) 9/6 - 6")

        test2 = Square(1, 1, 1, 1)
        self.assertEqual(test2.__str__(), "[Square] (1) 1/1 - 1")
        test2.update(id=37)
        self.assertEqual(test2.__str__(), "[Square] (37) 1/1 - 1")
        test2.update(size=3)
        self.assertEqual(test2.__str__(), "[Square] (37) 1/1 - 3")
        test2.update(x=4, y=5)
        self.assertEqual(test2.__str__(), "[Square] (37) 4/5 - 3")
        test2.update(id=35, size=4, x=5, y=1)
        self.assertEqual(test2.__str__(), "[Square] (35) 5/1 - 4")

        test2.update(2, 3, x=5, y=1)
        self.assertEqual(test2.__str__(), "[Square] (2) 5/1 - 3")

    def check_dic_isequal(self):
        """checks if value of to_dicionary() is actually accurate"""
        dic = {'size': 8, 'x': 1, 'y': 2, 'id': 99}
        sqr = Square(10, 1, 2, 99)
        sqrDict = sqr.to_dictionary()
        self.assertEqual(dic, sqrDict)

    def test_docstrings(self):
        """checks if Square has a docstring"""
        self.assertEqual(len(Square.__doc__) > 0, True)
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(Square.__init__.__doc__)
        self.assertTrue(hasattr(Square, "size"))
        self.assertTrue(Square.size.__doc__)
        self.assertTrue(hasattr(Square, "__str__"))
        self.assertTrue(Square.__str__.__doc__)
        self.assertTrue(hasattr(Square, "update"))
        self.assertTrue(Square.update.__doc__)
        self.assertTrue(hasattr(Square, "to_dictionary"))
        self.assertTrue(Square.to_dictionary.__doc__)
