#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0 or my_list is None:
        return

    max_value = 0
    for value in my_list:
        if value > max_value:
            max_value = value

    return (max_value)
