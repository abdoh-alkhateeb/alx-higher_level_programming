#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    numeral = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    numeral_count = len(roman_string)
    number = 0

    for i in range(numeral_count):
        value = numeral[roman_string[i]]
        if i < numeral_count - 1 and numeral[roman_string[i + 1]] > value:
            number -= value
        else:
            number += value

    return number
