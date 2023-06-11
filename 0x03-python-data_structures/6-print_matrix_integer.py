#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            if i != 0:
                print(" ", end='')
            print("{:d}".format(matrix[j][i]), end='')

        print()
