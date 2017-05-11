#!/usr/bin/python3
def complex_delete(my_dict, value):
    if value not in my_dict.values() or len(my_dict) == 0:
        return(my_dict)
    delete = [key for key in my_dict if my_dict[key] == value]
    print(delete)
    for key in delete:
        del(my_dict[key])
    return(my_dict)
