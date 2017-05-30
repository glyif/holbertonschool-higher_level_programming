#!/usr/bin/pyton3
"""
Square - inhereist from rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
        __init__
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        __str__ documentation
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """
        return area
        """
        return (self.__size * self.__size)
