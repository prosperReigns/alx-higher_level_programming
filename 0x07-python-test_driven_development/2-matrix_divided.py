#!/usr/bin/python3
""" a program that divides all the element in a matrix"""


def matrix_divided(matrix, div):
    """ a program that divides"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")

    new_list = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix \
                            (list of lists) of integers/floats")

    first_row = len(matrix[0])

    for row in matrix[1:]:
        if len(row) != first_row:
            raise TypeError("Each row of the matrix \
                            must have the same size")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix \
                            (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        row_result = []

        for element in row:
            if isinstance(element, (int, float)):
                row_result.append(round(element / div, 2))
            else:
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")

        new_list.append(row_result)
    return new_list
