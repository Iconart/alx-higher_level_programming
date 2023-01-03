#!/usr/bin/python3
"""A module to Divide  a matrix."""

def matrix_divided(matrix, div):
    """Divide matrix by div

    Agrs:
        matrix: A list of lists of integer
        div: An integer to divide all the list of lists

    Raises:
        TypeError: if matrix is not a list of lists of interer or float
        TypeError: if the length matrix rows are not equal
        TypeError: if div is not an integer or a float
        ZeroDivisionError: if div is equal to zero
    
    Returns:
        list: list of lists representing divided matrix
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " + "of integers/floats")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TyperError("matrix must be a matrix (list of lists) " + "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not instance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " + "of integers/floats")
    return [[round(x/div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
