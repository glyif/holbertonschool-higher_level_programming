#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 97 <= ord(i) <= 122:
            char = chr(ord(char) - 32)
        print("{:s}".format(char), end="")
    print('')
