#!/usr/bin/python3
"""smae class"""


def is_same_class(obj, a_class):
    """check if instances are the same

    Arguments:
        obj {object} -- object to be checked
        a_class {class} -- class to be checked

    Returns:
        bool -- True if they are same type, false otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
