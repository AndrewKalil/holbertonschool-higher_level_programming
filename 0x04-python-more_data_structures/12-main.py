#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CDXCIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XCIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XLIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XLIV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "I"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "III"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
