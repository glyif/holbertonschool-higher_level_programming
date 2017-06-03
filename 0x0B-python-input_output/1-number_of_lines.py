#!/usr/bin/python3


def number_of_lines(filename=""):
    """
    number_of_lines - counts number of lines

    Args:
    @filename: filename to open

    Return: number of lines
    """

    i = 0
    with open(filename, "r") as fd:
        for line in fd:
            i += 1
    return (i)
