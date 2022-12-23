#!/usr/bin/python3
"""Square module - setter and getter"""


class Square:
    """Define a square"""

    def __init__(self, size):
        """Initialise size"""
        self.size = size

    @property
    def size(self):
        return self.__size
    """Get the size property"""

    @size.setter
    def size(self, value):
        """Set the size values"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        """Handle the Exceptions errors"""

        self.__size = value

    def area(self):
        return self.__size ** 2
