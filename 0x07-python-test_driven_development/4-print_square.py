#!/usr/bin/python3
"""A module to Print square"""

def print_square(size):
    """Print square

    Agrs:
        size: the length and width of the square must be equal to size
    Raises:
        TypeError: the data type of the size is not integer
        ValueError: size is less than 0
        TypeError: the data type is float and it is less 0
    Returns:
        print hash(#) to form square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for a in range(0, size + 1):
        print()
        for b in range(0, size):
            print("#", end="")
