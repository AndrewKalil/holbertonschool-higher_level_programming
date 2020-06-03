#!/usr/bin/python3
"""write to a text file"""


def write_file(filename="", text=""):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        text {str} -- [description] (default: {""})

    Returns:
        [type] -- [description]
    """
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(text)
    return len(text)
