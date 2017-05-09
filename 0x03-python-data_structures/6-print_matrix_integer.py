#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    string = ''
    for list in matrix:
        string += "\n"
        for element in row:
            string += "{:d} ".format(element)
        string = string[:-1]

    print (string[1:])
