#!/usr/bin/python3
import json
"""Save Object to file"""


def save_to_json_file(my_obj, filename):
    """saves an object to json file

    Arguments:
        my_obj {object} -- object to be inputed
        filename {str} -- name of file
    """
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(json.dumps(my_obj))
