#!/usr/bin/python3
# This prints a string into an upper case string


def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print('{:s}'.format(i), end="")
    print('')
