#!/usr/bin/python3
"""square module"""


class Square:
    """Define a square"""
    def __init__(self, size=0):
        """the value of size should be integer"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method for area"""
        return self.__size ** 2
