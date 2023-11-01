#!/usr/bin/python3
"""
Module that has the definition of text_indentation function.
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after
    each of these characters: { ., ?, : }
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delimiter in ".:?":
        text = (delimiter + "\n\n").join(
            [line.strip() for line in text.split(delimiter)])

    print(text, end="")
