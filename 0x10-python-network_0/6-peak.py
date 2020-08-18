#!/usr/bin/python3
"""  """


def find_peak(list_of_integers):
    if list_of_integers == []:
        return
    max = 0
    for i in list_of_integers:
        if i > max:
            max = i
    return (max)
