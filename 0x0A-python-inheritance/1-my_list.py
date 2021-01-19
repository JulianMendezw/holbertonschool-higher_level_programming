#!/usr/bin/python3
""" A class MyList that inherits from list """


class MyList(list):
    """ Subclass that inherits from list """

    def print_sorted(self):
        """ Method instance that prints a sorted list """
        print(sorted(self))
