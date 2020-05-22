#!/usr/bin/python3
"""Module that prints a name
"""


def say_my_name(first_name, last_name=""):
    """prints name with arguements given

    Arguments:
        first_name {str} -- first name

    Keyword Arguments:
        last_name {str} -- first name (default: {""})

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
