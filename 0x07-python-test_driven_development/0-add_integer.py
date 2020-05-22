#!/usr/bin/python3
"""Simple addition
"""


def add_integer(a, b=98):
    """Adds two variables and returns an int

    Arguments:
        a {int or float} -- variable containing a number

    Keyword Arguments:
        b {int or float} -- variable containing a number (default: {98})

    Raises:
        TypeError: In the case that input arguement is not an int
        TypeError: In the case that input arguement is not an int

    Returns:
        int -- Result of the addition
    """
    result = 0
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    result = a + b
    return result
