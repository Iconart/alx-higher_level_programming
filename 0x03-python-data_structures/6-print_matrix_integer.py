#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for submat in matrix:
        print(" ")
        for element in submat:
            print("{:d}".format(element), end="")
