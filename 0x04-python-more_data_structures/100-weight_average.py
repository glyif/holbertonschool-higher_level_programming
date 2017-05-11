#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return(0)
    result = [0, 0]
    for tuples in my_list:
        if (len(tuples) != 2):
            return
        result[0] += tuples[0] * tuples[1]
        result[1] += tuples[1]
    return(result[0]/result[1])
