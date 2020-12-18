#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = a_dictionary.copy()
    for i, x in copy.items():
        if x == value:
            a_dictionary.pop(i)

    return a_dictionary
