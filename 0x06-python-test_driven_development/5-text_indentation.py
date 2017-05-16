#!/usr/bin/python3
"""
``5-text_indentation`` module
This module creates a new line after every period.

Example:
>>> text_indentation("hello there. my name is bobby.")
hello there.

my name is bobby.

"""


def is_space(char):
    """
    is_space: checks if it's a delimiter

    Arguments:
    char -- character

    Return:
    True or False
    """

    if char == ':':
        return(False)
    elif char == '.':
        return(False)
    elif char == '?':
        return(False)

    return(True)

def text_indentation(text):
    """
    text_indentation: prints indents text with 2 spaces if following `:`, `.` or `?`
    
    Arguments:
    text -- string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text_list = []
    
    #if flag is 0, new line.
    flag = 0
    inside = 0

    for i in range(0, len(text)):
        
        if flag == 2:
            text_list.append('\n')
            flag = 0
            if text[i] == " ":
                continue

        if is_space(text[i]):
            text_list.append(text[i])
            flag = 0
        else:
            text_list.append(text[i])
            flag = 1

        if flag is 1:
            text_list.append('\n')
            flag = 2

        i += 1

    str1 = ''.join(str(e) for e in text_list)

    print(str1)
