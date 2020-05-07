#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    num = 0
    for i in my_list:
        if i not in new:
            new.append(i)
            num += i
    return num
