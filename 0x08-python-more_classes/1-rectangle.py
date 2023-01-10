#!/usr/bin/python3
"""Rectangle module"""

class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialise width and heigt"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrive the width"""
        return self.__width
        
    @width.setter
    def width(self, value):
        """Set the width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
            
    @property
    def height(self):
        """Retrieve the height"""
        return self.__height
        
    @height.setter
    def height(self, value):
        """Set the height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
