#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        j = 0
        for i in my_list:
            if i > j:
                j = i
    return(j if my_list else None)
