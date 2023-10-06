#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence)
    return (strlen, None if strlen == 0 else sentence[0])
