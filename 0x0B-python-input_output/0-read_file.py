#!/usr/bin/python3
"""reads a file and prints content"""


def read_file(filename=""):
    """opens a file and prints text

    Keyword Arguments:
        filename {str} -- name of file (default: {""})
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
