#!/usr/bin/python3
def multiply_by_2(my_dict):
    if my_dict is None or len(my_dict) == 0:
        return

    new_dict = dict(my_dict)
    for key in new_dict:
        new_dict[key] = new_dict[key] * 2
    return(new_dict)
