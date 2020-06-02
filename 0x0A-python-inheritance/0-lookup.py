#!/usr/bin/python3
"""Used to shows available attributes for the object"""


def lookup(obj):
    """function that returns available attributes

    Arguments:
        obj {object} -- type object

    Returns:
        list -- list of available attributes
    """
    return list(dir(obj))
