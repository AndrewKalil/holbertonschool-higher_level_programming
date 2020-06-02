#!/usr/bin/python3
"""Geometry class"""


class BaseGeometry:
    """BAse funcitons of geometry
    """
    def area(self):
        """area of shape

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator

        Arguments:
            name {string} -- name of value to be validated
            value {int} -- value to be validated

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
