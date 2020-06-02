#!/usr/bin/python3
"""inherit list"""


class MyList(list):
    """Does same as list but sorted

    Arguments:
        list {list} -- object "list"
    """
    def print_sorted(self):
        """prints a list sorted
        """
        print(sorted(self))
