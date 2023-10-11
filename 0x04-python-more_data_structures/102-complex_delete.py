#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return dict(filter(lambda k, v: v == value, a_dictionary))
