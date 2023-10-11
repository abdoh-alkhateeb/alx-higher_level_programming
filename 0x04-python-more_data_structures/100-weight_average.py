#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    sum = 0
    count = 0

    for pair in my_list:
        sum += pair[0] * pair[1]
        count += pair[1]

    return sum / count
