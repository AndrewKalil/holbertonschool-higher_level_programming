#!/usr/bin/python3
"""Rectanlge Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square

    Arguments:
        Rectangle {class} -- class from which current class was inherited
    """
    def __init__(self, size):
        """Instantiation for square class

        Arguments:
            size {int} -- size of one side of the square
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)
