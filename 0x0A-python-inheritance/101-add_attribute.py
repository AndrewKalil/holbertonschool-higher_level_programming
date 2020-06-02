#!/usr/bin/python3
def add_attribute(cls, field, name):
    """add a new attribute

    Arguments:
        field {str} -- field to be added as attribute
        name {str} -- value for field

    Raises:
        TypeError: can't add new attribute
    """
    if not hasattr(cls, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(cls, field, name)
