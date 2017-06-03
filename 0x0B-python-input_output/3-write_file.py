#!/usr/bin/python3


def write_file(filename="", text=""):
    """
    write_file - writes to file

    Args:
    @filename: filenmae
    @text: text to write

    Return: characters written
    """
    with open(filename, mode="w", encoding="utf-8") as fd:
        return (fd.write(text))
