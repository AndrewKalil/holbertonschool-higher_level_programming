#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None
    length = len(sentence)
    if length > 0:
        tuple_lf = (length, sentence[0])
        return tuple_lf
