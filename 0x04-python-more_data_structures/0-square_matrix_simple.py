#!/usr/bin/python3
def squared(x):
    return x**2


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(squared, i)))
    return new_matrix
