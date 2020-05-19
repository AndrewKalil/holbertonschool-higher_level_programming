#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation

        Keyword Arguments:
            size {int} -- size of the square (default: {0})
            position {tuple} -- position of the square (default: {(0,0)})
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ retrive positional value

        Returns:
            tuple -- tuple containing coordinates of position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets new position

        Arguments:
            value {tuple} -- values to be set in tuple

        Raises:
            TypeError: Raises error if position is not a positive value
            TypeError: Raises error if position is not a positive value
            TypeError: Raises error if position is not a positive value
            TypeError: Raises error if position is not a positive value
        """
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int and type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """squares the size to compute the area of the square

        Returns:
            int -- area of square
        """
        return self.__size ** 2

    def my_print(self):
        """prints the sqaure according to the size
        """
        if self.__size == 0:
            print()
            return
        for p in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("{}{}".format(" "*self.__position[0], "#"*self.__size))
