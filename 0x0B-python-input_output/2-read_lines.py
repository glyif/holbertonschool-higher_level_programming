#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """
    read_line - reads file until nb_lines

    Args:
    @filename: file name
    @nb_line: lines to print
    """
    read_buffer = []

    with open(filename, "r", encoding="utf-8") as fd:
        count = 0
        for count, line in enumerate(fd):
            if (count < nb_lines or nb_lines == 0):
                read_buffer.append(line)
            else:
                break

        print("{}".format("".join(read_buffer)), end="")
