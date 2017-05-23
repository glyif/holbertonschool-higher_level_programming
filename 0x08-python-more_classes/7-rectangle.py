#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """
    Rectangle class
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        initializes width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        destructor
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        width property
        """
        return (self.__width)

    @property
    def height(self):
        """
        height property
        """
        return (self.__height)

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        returns area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        returns perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)

        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        informal string representation
        """
        matrix = [str(self.print_symbol) * self.__width
                  for row in range(0, self.__height)]
        return ("{:s}".format('\n'.join(matrix)))

    def __repr__(self):
        """
        formal string representaion
        """
        rep = (self.__width, self.__height)
        return ("Rectangle{:s}".format(str(rep)))
