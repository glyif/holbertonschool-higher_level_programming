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
        self.__size = size

    @property
    def size(self):
        """
        getting value of size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setting value to self
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Area:
        returns the area of the circle
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        prints square
        """
        matrix = ['#' * self.__size for i in range(0, self.__size)]

        print("{:s}".format('\n'.join(matrix)))
