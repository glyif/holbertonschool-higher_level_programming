#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for thing in my_list:
        if type(thing) is int:
            print("{:d}".format(thing))
