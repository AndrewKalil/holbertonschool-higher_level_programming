#!/usr/bin/python3
"""Geometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherited class from Rectangle

    Arguments:
        BaseGeometry {class} -- base class fro rectangle class
    """
    def __init__(self, width, height):
        """instantiation of rectanlge objects

        Arguments:
            width {int} -- width of rectangle
            height {int} -- height of rectangle
        """
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        """method to find area of rectangle

        Returns:
            int -- area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """constructs a string

        Returns:
            [str] -- string to be returned
        """
        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string
