#!/usr/bin/python3
"""
Square Module:
defines a square
"""

class Square:
    """
    Square class:
    defines an instance of a square
    """
    def __init__(self, size=0):
        """
        __init__:
        initializes the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Area:
        returns the area of the circle
        """
        return(self.__size * self.__size)
