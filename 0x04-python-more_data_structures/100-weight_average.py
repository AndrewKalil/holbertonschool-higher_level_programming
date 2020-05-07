#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    den = 0
    if my_list:
        for i in my_list:
            num += i[0] * i[1]
            den += i[1]
        avg = num / den
        return avg
    return 0
