#!/usr/bin/python3


def no_c(my_string):
    x = len(my_string)
    for i in range(0, x):
        if my_string[i] == 'c' or my_string[i] == 'C':
            copy = my_string[0:i] + my_string[i + 1:x]

    return(copy)
