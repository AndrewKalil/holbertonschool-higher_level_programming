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

    def area(self):
        """area of rectangle

        Returns:
            int -- area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of rectangle

        Returns:
            int -- perimeter of rectangle
        """
        if self.__height is 0 or self.__width is 0:
            return 0
        return (2*self.__height) + (2*self.__width)
