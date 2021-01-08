#!/usr/bin/python3
"""a function that prints a text with 2 new lines after each
of these characters: ., ? and :"""


def text_indentation(text):
    """a function that prints a text with 2 new lines"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    cpy_text = text.strip()

    i = ''
    for i in cpy_text:
        print(i, end="")
        if i == '.' or i == '?' or i == ':':
            print('\n')
