#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """inverts operators for ints

    Arguments:
        int {class} -- class being inherited
    """
    def __init__(self, number):
        """Instantiation of class

        Arguments:
            number {int} -- value to check
        """
        self.__integer = number

    def __eq__(self, other):
        """changes == to !=

        Arguments:
            other {int} -- arguement to be passed to check

        Returns:
            bool -- False instead of true
        """
        return self.__integer != other  # or False

    def __ne__(self, other):
        """changes != to ==

        Arguments:
            other {int} -- arguement to be passed to check

        Returns:
            bool -- True instead of false
        """
        return not self.__integer != other  # or True

    def __str__(self):
        """returns a string to print

        Returns:
            str -- integer caster as string
        """
        return str(self.__integer)
