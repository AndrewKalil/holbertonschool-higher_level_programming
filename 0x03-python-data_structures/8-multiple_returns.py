#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None
    tuple_lf = (len(sentence), sentence[0])
    return tuple_lf
