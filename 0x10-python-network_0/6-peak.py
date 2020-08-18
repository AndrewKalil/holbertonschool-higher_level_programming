#!/usr/bin/python3
""" find the peak of a list """


def find_peak(list_of_integers):
    """ find the peak of a list"""
    if list_of_integers == [] or list_of_integers is None:
        return None
    max = 0
    for i in list_of_integers:
        if i > max:
            max = i
    return (max)
