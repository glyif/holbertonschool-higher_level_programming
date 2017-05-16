#!/usr/bin/python3
"""
This is a module that concats two strings with a space in between.

For example,
>>> say_my_name("Bobby", "Yang")
Bobby Yang
"""

def say_my_name(first_name, last_name=""):
    """
    say_my_name concats 2 strings with a space in between

    Arguments:
    first_name -- string
    last_name -- string (optional)

    both arguments need to be strings or error is raised
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
