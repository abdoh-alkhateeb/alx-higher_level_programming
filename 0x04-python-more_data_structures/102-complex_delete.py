#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []

    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys.append(key)

    for key in keys:
        del a_dictionary[key]

    return a_dictionary
