#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    i = 0
    for element in string_list:
        if element == 'c' or element == 'C':
            del string_list[i]
            i = i + 1
    return (''.join(string_list))
