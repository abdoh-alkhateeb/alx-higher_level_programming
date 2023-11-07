#!/usr/bin/python3
"""
Module that defines pascal_triangle function.
"""


def factorial(n):
    """
    Function that returns factorial of number n.
    """

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def pascal_triangle(n):
    """
    Function that returns matrix of ints representing Pascal's triangle of n.
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []

        for j in range(i + 1):
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))

        triangle.append(row)

    return triangle
