#!/usr/bin/python3
"""Module that sepates a text
"""


def text_indentation(text):
    """separates a text into senteces separated by certain characters

    Arguments:
        text {str} -- string to be splitted

    Raises:
        TypeError: text must be a string
    """
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    print("\n".join(i.lstrip() for i in text.split("\n")), end="")
