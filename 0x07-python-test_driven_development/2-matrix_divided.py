#!/usr/bin/python3
"""
Module that has the definition for the function matrix_divided.
"""


def matrix_divided(matrix, div):
    """
    Function that that divides all elements of a matrix and returns result.
    """

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(error_msg)

    if len(matrix) != 0:
        row_len = len(matrix[0])

    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)

        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(error_msg)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = []

        for element in row:
            new_row.append(round(element / div, 2))

        new_matrix.append(new_row)

    return new_matrix
