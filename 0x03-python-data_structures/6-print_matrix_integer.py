#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for i in range(len(matrix)):
        d = ""
        for j in range(len(matrix[i])):
            print("{:s}{:d}".format(d, matrix[i][j]), end='')
            d = " "
        print()
