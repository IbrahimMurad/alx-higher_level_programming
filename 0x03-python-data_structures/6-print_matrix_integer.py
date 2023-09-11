#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_len = len(row)
        if row_len == 0:
            return
        for i in range(row_len - 1):
            print("{:d}".format(row[i]), end=' ')
        print("{:d}".format(row[row_len - 1]))
