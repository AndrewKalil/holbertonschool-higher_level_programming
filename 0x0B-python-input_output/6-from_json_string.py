#!/usr/bin/python3
import json
"""From JSON string to Object"""


def from_json_string(my_str):
    """from json to object

    Arguments:
        my_str {json} -- object to convert

    Returns:
        object -- object representation
    """
    return json.loads(my_str)
