#!/usr/bin/python3
"""
This is a module that adds two integers.

For example,
>>> add_integer(10, 15)
35
"""


def add_integer(a, b):
    """
    add_integer adds 'a' and 'b' and returns the sum

    Arguments:
    a -- integer 1
    b -- integer 2

    if a != int or b != int:
        throw type error
    else:
        return sum of 'a' and 'b'

    floats are casted into integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return(int(a) + int(b))
