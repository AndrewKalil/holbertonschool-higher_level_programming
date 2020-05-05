#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    for i in range(len(my_list)):
        if idx > i:
            return my_list
        elif i == idx:
            my_list[i] = element
            return my_list
