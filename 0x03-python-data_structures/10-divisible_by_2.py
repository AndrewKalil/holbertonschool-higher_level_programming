#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for i in my_list:
        if my_list[i] % 2 == 0:
            new.append(True)
        elif my_list[i] % 2 != 0:
            new.append(False)
    return new
