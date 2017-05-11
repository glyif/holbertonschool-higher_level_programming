#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda lists: (list(map(lambda k: k*k, lists))), matrix))
