#!/usr/bin/python3
"""Base unitests"""
from models.rectangle import Rectangle
from io import StringIO
import unittest
import sys


class BaseTest(unittest.TestCase):
    """tests for base class"""

    def test_init(self):
        """checking instantiation method"""
        test1 = Rectangle(3, 9)
        self.assertEqual(test1.width, 3)
        self.assertEqual(test1.height, 9)
        self.assertEqual(test1.x, 0)
        self.assertEqual(test1.y, 0)

        test2 = Rectangle(2, 4, 3, 1, 11)
        self.assertEqual(test2.width, 2)
        self.assertEqual(test2.height, 4)
        self.assertEqual(test2.x, 3)
        self.assertEqual(test2.y, 1)
        self.assertEqual(test2.id, 11)

        test3 = Rectangle(5, 3, 2)
        self.assertEqual(test3.width, 5)
        self.assertEqual(test3.height, 3)
        self.assertEqual(test3.x, 2)
        self.assertEqual(test3.y, 0)

    def test_possible_TypeError_rasies(self):
        """ensures all possible raises are covered for creating a rectangle"""
        with self.assertRaises(TypeError):
            Rectangle("3", 4)

        with self.assertRaises(TypeError):
            Rectangle(3, "4")

        with self.assertRaises(TypeError):
            Rectangle(5, 4, "1", 5)

        with self.assertRaises(TypeError):
            Rectangle(5, 4, 1, "5")

    def possible_update_TypeErrors(self):
        """checking value erros when updating"""
        test = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            test.update(1, "3", 4)

        with self.assertRaises(TypeError):
            test.update(1, "3", 4)

        with self.assertRaises(TypeError):
            test.update(1, 5, 4, "1", 5)

        with self.assertRaises(TypeError):
            test.update(1, 5, 4, 1, "5")

    def test_possible_ValueError_rasies(self):
        """ensures all possible raises are covered for creating a rectangle"""
        with self.assertRaises(ValueError):
            Rectangle(-5, 4)

        with self.assertRaises(ValueError):
            Rectangle(5, -4)

        with self.assertRaises(ValueError):
            Rectangle(5, 0)

        with self.assertRaises(ValueError):
            Rectangle(0, 4)

        with self.assertRaises(ValueError):
            Rectangle(5, 4, -1, 5)

        with self.assertRaises(ValueError):
            Rectangle(5, 4, 1, -5)

    def possible_update_VaueErrors(self):
        """checking type errors when updating"""
        test = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            test.update(1, 3, -4)

        with self.assertRaises(ValueError):
            test.update(height=-4)

        with self.assertRaises(ValueError):
            test.update(1, -3, 4)

        with self.assertRaises(ValueError):
            test.update(width=-3)

        with self.assertRaises(ValueError):
            test.update(1, 5, 4, -1, 5)

        with self.assertRaises(ValueError):
            test.update(x=-1)

        with self.assertRaises(ValueError):
            test.update(1, 5, 4, 1, -5)

        with self.assertRaises(ValueError):
            test.update(y=-5)

    def test_area(self):
        """testing the area for the rectangle method"""
        test1 = Rectangle(4, 5)
        self.assertEqual(test1.area(), 20)

        test2 = Rectangle(5, 9, 45, 100)
        self.assertEqual(test2.area(), 45)

    def test_display(self):
        """testing the display printed to the stdout"""
        output = StringIO()
        sys.stdout = output

        test1 = Rectangle(4, 5)
        test1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            output.getvalue(), "####\n####\n####\n####\n####\n")

    def test_display_with_shift(self):
        """testing the display printed to the stdout"""
        output = StringIO()
        sys.stdout = output

        test2 = Rectangle(2, 3, 1, 2)
        test2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            output.getvalue(), "\n\n ##\n ##\n ##\n")

    def test_str_for_rectangle(self):
        """testing the string to be printed from __str__"""
        test1 = Rectangle(3, 4, 3, 2, 10)
        self.assertEqual(test1.__str__(), "[Rectangle] (10) 3/2 - 3/4")

    def test_update_with_args_and_kwargs(self):
        """testing if update actually updates an object"""
        test1 = Rectangle(3, 4, 3, 2, 10)
        self.assertEqual(test1.__str__(), "[Rectangle] (10) 3/2 - 3/4")
        test1.update(69)
        self.assertEqual(test1.__str__(), "[Rectangle] (69) 3/2 - 3/4")
        test1.update(69, 6)
        self.assertEqual(test1.__str__(), "[Rectangle] (69) 3/2 - 6/4")
        test1.update(69, 6, 9)
        self.assertEqual(test1.__str__(), "[Rectangle] (69) 3/2 - 6/9")
        test1.update(69, 6, 9, 6)
        self.assertEqual(test1.__str__(), "[Rectangle] (69) 6/2 - 6/9")
        test1.update(69, 6, 9, 6, 9)
        self.assertEqual(test1.__str__(), "[Rectangle] (69) 6/9 - 6/9")

        test2 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(test2.__str__(), "[Rectangle] (1) 1/1 - 1/1")
        test2.update(id=37)
        self.assertEqual(test2.__str__(), "[Rectangle] (37) 1/1 - 1/1")
        test2.update(width=2, height=3)
        self.assertEqual(test2.__str__(), "[Rectangle] (37) 1/1 - 2/3")
        test2.update(x=4, y=5)
        self.assertEqual(test2.__str__(), "[Rectangle] (37) 4/5 - 2/3")
        test2.update(id=35, width=3, height=4, x=5, y=1)
        self.assertEqual(test2.__str__(), "[Rectangle] (35) 5/1 - 3/4")

        test2.update(2, 3, 4, x=5, y=1)
        self.assertEqual(test2.__str__(), "[Rectangle] (2) 5/1 - 3/4")

    def check_dic_isequal(self):
        """checks if value of to_dicionary() is actually accurate"""
        dic = {'width': 10, 'height': 8, 'x': 1, 'y': 2, 'id': 99}
        rec = Rectangle(10, 8, 1, 2, 99)
        recDict = rec.to_dictionary()
        self.assertEqual(dic, recDict)

    def test_docstrings(self):
        """checks if Rectangle has a docstring"""
        self.assertEqual(len(Rectangle.__doc__) > 0, True)
