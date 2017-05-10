#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    string = ''
    for lists in matrix:
        string += "\n"
        for element in lists:
            string += "{:d} ".format(element)
        string = string[:-1]

    print(string[1:])
