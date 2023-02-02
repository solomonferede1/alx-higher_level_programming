#!/usr/bin/python3
"""
The 2-matrix_divide module
"""


def matrix_divided(matrix, div):
    """matrix_divided function that divides all elements of a matrx"""
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    if type(matrix) != list or any(type(lst) is not list for lst in matrix) \
       or len(matrix) == 0 or any(len(lst) == 0 for lst in matrix):
        raise TypeError(err1)
    for lst in matrix:
        for n in lst:
            if not type(n) in [int, float]:
                raise TypeError(err1)
    if any(len(matrix[0]) != len(lst) for lst in matrix):
        raise TypeError(error2)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    return [[round(num / div, 2) for num in lst] for lst in matrix]
