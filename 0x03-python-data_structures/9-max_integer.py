#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0 or my_list is None:
        return(None)

    max_value = my_list[0]
    for value in my_list:
        if value >= max_value:
            max_value = value

    return(max_value)
