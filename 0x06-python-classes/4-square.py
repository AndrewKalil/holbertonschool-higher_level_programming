#!/usr/bin/python3
class Square:
    """class Square
    """
    def __init__(self, size=0):
        """Instantiation

        Keyword Arguments:
            size {int} -- size of the square (default: {0})

        Raises:
            TypeError: Raises error if type of var size in not int
            ValueError: Raises error if value if is out of range
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """retrieves the size of the square

        Returns:
            int -- size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets new value to the size of the square

        Arguments:
            value {int} -- new value of size to be set

        Raises:
            TypeError: Raises error if variable size is not an integer
            ValueError: Raises error if size is out of rang or a negative value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """squares the size to compute the area of the square

        Returns:
            int -- area of square
        """
        return self.__size**2
