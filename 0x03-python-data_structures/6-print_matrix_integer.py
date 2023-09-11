#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_len = len(row)
        if row_len == 0:
            return
        for i in row[:-1]:
            print("{:d}".format(i), end=' ')
        print("{:d}".format(row[-1]))
