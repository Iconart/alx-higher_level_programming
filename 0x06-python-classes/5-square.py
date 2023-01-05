#!/usr/bin/python3
"""square module - print hash in matrix form"""


class Square:
    """Define a square"""

    def __init__(self, size):
        """Initialise size field"""
        self.size = size
    @property
    def size(self):
        """Get the size variable"""
        return self.__size = size
    @size.setter
    def size(self, value):
        """Set the a new value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """square the value in size"""
        return self.__size ** 2
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in (0, self.__size):
                for j in (0, self.__size):
                    print("#", end='')
                print('\n')
my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")
