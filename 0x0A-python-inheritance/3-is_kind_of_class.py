#!/usr/bin/python3
"""isinstance"""


def is_kind_of_class(obj, a_class):
    """check if instances are the same or if the obj was inherited from class

    Arguments:
        obj {object} -- object to be checked
        a_class {class} -- class to be checked

    Returns:
        bool -- True if they are same type, false otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
