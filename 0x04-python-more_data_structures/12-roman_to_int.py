#!/usr/bin/python3
def roman_to_int(roman_string):
    s = roman_string
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is not None or type(roman_string) == str:
        num = 0
        for i in range(len(roman_string)):
            if (i > 0 and dic[s[i]] > dic[s[i - 1]]):
                first = dic[s[i]]
                second = dic[s[i - 1]]
                num += first - second * 2
            else:
                first = dic[s[i]]
                num += first
        return num
    return 0
