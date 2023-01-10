#!/usr/bin/python3
"""Rectangle module"""

class Rectangle:
    """Area and perimeter class"""
    def __init__(self, width=0, height=0):
        """Initialise width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return the height"""
        return self.__width

    @height.setter
    def height(self, value):
        """Set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of a rectangle"""
        return self.__width * 2 + self.__height * 2
    

