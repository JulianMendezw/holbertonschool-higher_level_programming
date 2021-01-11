#!/usr/bin/python3
"""Define a Rectangle"""


class Rectangle:
    """A class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
