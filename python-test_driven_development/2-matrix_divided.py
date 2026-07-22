#!/usr/bin/python3
"""Module for dividing all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix (list): a list of lists of integers or floats.
        div (int/float): the number to divide each element by.

    Returns:
        list: a new matrix with all elements divided by div,
            rounded to 2 decimal places.
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix) or
            not all(
                isinstance(num, (int, float)) and not isinstance(num, bool)
                for row in matrix for num in row
            )):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
