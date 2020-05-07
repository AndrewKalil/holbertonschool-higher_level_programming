#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for i in a_dictionary.keys():
        num = a_dictionary[i] * 2
        new_dic[i] = num
    return new_dic
