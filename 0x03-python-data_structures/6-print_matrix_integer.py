#!/usr/bin/python3
def print_list(matrix_list=[]):
    for n in range(0, len(matrix_list)):
        if n < len(matrix_list) - 1:
            print("{:d}".format(matrix_list[n]), end=" ")
        else:
            print("{:d}".format(matrix_list[n]))


def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        i = 0
        new_list = []
        for char in list:
            new_list.append(char)
            length = len(new_list)
        print_list(new_list)
