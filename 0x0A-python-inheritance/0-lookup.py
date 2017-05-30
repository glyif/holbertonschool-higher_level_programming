#!/usr/bin/python3


def lookup(obj):
    """
    lookup - returns list of avail attributes and methods of an obj

    Args:
    @obj: object to extract

    Return: list of avail attributes and methods of an object
    """
    return(list(dir(obj)))
