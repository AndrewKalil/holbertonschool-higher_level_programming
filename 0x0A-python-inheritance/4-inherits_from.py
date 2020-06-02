#!/usr/bin/python3
"""check if inherited"""


def inherits_from(obj, a_class):
    """check if instances are the same or if the obj was inherited from class

    Arguments:
        obj {object} -- object to be checked
        a_class {class} -- class to be checked

    Returns:
        bool -- True if they are same type, false otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False