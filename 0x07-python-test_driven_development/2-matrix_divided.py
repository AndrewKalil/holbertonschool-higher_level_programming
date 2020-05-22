#!/usr/bin/python3
"""Module that divides two numbers
"""


def matrix_divided(matrix, div):
    """dives each element of the matrix by div

    Arguments:
        matrix {list} -- double list countaining int or floats
        div {int or float} -- number diving each element

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns:
        int or float -- list of quotients
    """
    L = []
    if not isinstance(matrix, list) or\
       not all(isinstance(i, list) for i in matrix) or\
       not all(isinstance(j, (int, float)) for i in matrix for j in i):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        L.append([])
        for j in range(len(matrix[i])):
            L[i].append(round(matrix[i][j]/div, 2))
    return L
