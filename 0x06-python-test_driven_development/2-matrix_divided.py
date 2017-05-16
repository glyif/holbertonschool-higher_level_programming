#!/usr/bin/python3
"""
This is a module that divides all elements of a matrix by a number.

For example,
>>> matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def check_matrix(matrix):
    """
    check_matrix checks the passed in `matrix` to see if it's valid

    Arguments:
    matrix -- matrix (list of lists)

    Checks to see if all elements are ints or floats
    checks to see if all rows are same length

    Return:
        True for valid matix
    or
        1 if not all elements are ints or floats
    or
        2 if not all rows are same length
    """

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            return(2)
        for element in row:
            if not isinstance(element, (int, float)) \
                    or isinstance(element, bool):
                return(1)

    return(0)


def matrix_divided(matrix, div):
    """
    matrix_divided takes all elements of the `matrix` and divides by `div`

    Arguments:
    matrix -- matrix (list of lists)
    div -- to divide by

    All elements need to be ints or floats or error is raised.
    Every row need to have the same length or error is raised.
    Div cannot be zero or error is raised.

    Return:
        list of lists with divided elements (floats with 2 decimals)
    or
        Error is Raised
    """

    check_result = check_matrix(matrix)
    new_matrix = []
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    if check_result == 1:
        raise TypeError(matrix_error)
    elif check_result == 2:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        quotients = []
        for element in row:
            quotients.append(round(element / div, 2))
        new_matrix.append(quotients)

    return(new_matrix)
