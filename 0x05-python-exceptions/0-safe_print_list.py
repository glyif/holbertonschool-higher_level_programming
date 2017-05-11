#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for element in my_list:
        if i < x:
            try:
                print("{}".format(element), end="")
                i += 1
            except IndexError:
                print("")
                break
    print("")
    return(i)
