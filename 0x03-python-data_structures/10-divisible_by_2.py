#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return
    if len(my_list) == 0:
        return

    new_list = list(my_list)

    for element in my_list:
        if element % 2 == 0:
            new_list[element] = True
        else:
            new_list[element] = False

    return (new_list)
