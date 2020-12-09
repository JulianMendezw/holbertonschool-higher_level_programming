#!/usr/bin/python3


def remove_char_at(str, n):
    copy = ""
    index = 0
    for i in str:
        if index != n:
            copy += i
        index += 1
    return (copy)
