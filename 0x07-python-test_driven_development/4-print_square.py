#!/usr/bin/python3
""" Module that prints square
"""


def print_square(size):
    """prints a square according to size given

    Arguments:
        size {int} -- size of the square's side

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if not isinstance(size, int) or\
       type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
            print("{}".format("#"*size))
