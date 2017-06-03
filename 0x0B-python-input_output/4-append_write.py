#!/usr/bin/python3


def append_write(filename="", text=""):
    """
    append_write - appends to file

    Args:
    @filename: filename
    @text: text to append

    Return: character added
    """
    with open(filename,  mode='a') as fd:
        return (fd.write(text))
