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
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def position(self):
        """
        getting value of position
        """
        return (self.__position)

    @property
    def size(self):
        """
        getting value of size
        """
        return (self.__size)

    @position.setter
    def position(self, value):
        """
        setting position value with error check
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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
        prints the square
        """
        matrix = [' ' * self.__position[0] + '#' * self.__size
                  for i in range(0, self.__size)]
        print("{:s}".format('\n' * self.__position[1]), end="")
        print("{:s}".format('\n'.join(matrix)))
