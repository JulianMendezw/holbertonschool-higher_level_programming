#!/usr/bin/python3
""" emty doctstring """


class MyInt(int):
    """ A class MyInt that inherits from int """
    def __eq__(self, other):
        return self.numerator != other

    def __ne__(self, other):
        return self.numerator == other
