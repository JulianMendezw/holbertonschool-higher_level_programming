#!/usr/bin/python3
""" A function that returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ;
    otherwise False.
"""


def inherits_from(obj, a_class):
    """ A function that returns True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class;
        otherwise False.
    """

    return (True if isinstance(obj, a_class)
            and type(obj) is not a_class else False)
