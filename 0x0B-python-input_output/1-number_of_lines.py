#!/usr/bin/python3
"""Number of lines"""


def number_of_lines(filename=""):
    """number of lines

    Keyword Arguments:
        filename {str} -- name of file (default: {""})

    Returns:
        int -- number of lines in file
    """
    with open(filename) as myFile:
        return len(myFile.readlines())
