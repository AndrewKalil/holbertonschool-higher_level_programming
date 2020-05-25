#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Initialization

        Keyword Arguments:
            width {int} -- width of rectangle (default: {0})
            height {int} -- height of rectangle (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width of the rectangle

        Returns:
            int -- value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set value of width

        Arguments:
            value {int} -- set value of width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve height of rectancle

        Returns:
            int -- value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height of rectangle

        Arguments:
            value {int} -- set value of height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
