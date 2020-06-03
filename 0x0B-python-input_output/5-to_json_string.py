#!/usr/bin/python3
import json
"""To JSON string"""


def to_json_string(my_obj):
    """returns JSON representation of an object

    Arguments:
        my_obj {str} -- [description]

    Returns:
        json -- representation of a string
    """
    return json.dumps(my_obj)
