#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_row = len(matrix)
    len_col = len(matrix[0])
    for i in range(len_row):
        for j in range(len_col):
            print("{:d}".format(matrix[i][j]))
