#!/usr/bin/python3
"""
This file contains the ``3-print_square`` module

Example"
>>> print_square(5)
#####
#####
#####
#####
#####
"""


def print_square(size):
    """
    ``print_square`` is a function that prints a square of ``size`` l and w of `#`

    Arguments:
    size -- size a the square

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise TypeError("size must be >= 0")
    elif size is 0:
        print("")
        return

    for i in range (0, size):
        for i in range (0, size):
            print('#', end="")
        print("")
