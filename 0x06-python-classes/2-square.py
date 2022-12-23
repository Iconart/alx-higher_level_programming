#!/usr/bin/python3
"""Square module - checking"""


class Square:
    """Define square"""
    def __init__(self, size=0):
        """checking for some conditions to be meant"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
