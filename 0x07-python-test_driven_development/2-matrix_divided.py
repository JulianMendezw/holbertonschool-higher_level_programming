#!/usr/bin/python3
""" a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """ a function that divides all elements of a matrix."""

    message = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(message)

    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):

        if type(matrix[i]) is not list or len(matrix[i]) == 0:
            raise TypeError(message)

        if len(matrix[0]) != len(matrix[i]) or type(matrix[i]) is not list:
            raise TypeError("Each row of the matrix must have the same size")

        if isinstance(matrix[i], list) is False:
            raise TypeError(message)

        for x in range(len(matrix[i])):
            if isinstance(matrix[i][x], (int, float)) is False:
                raise TypeError(message)

    return [[round(x[i]/div, 2) for i in range(len(x))]for x in matrix]
