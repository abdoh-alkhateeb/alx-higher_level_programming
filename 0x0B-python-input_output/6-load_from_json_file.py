#!/usr/bin/python3
"""
Module that defines load_from_json_file function.
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file.
    """

    with open(filename, "r") as f:
        obj = json.loads(f.read())

    return obj
