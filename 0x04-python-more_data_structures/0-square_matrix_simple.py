def square_matrix_simple(matrix=[]):
    return list(map(lambda row: list(map(lambda c: c**2, row)), matrix))
