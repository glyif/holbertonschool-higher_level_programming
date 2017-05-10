#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return
    if len(my_list) == 0:
        return

    new_list = list(my_list)

    i = 0
    for element in my_list:
        if element % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
        i = i + 1
    return(new_list)
