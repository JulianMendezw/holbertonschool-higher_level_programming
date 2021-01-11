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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * 2 + self.__height * 2

    def __str__(self):
        string = ''

        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                string += "#" * self.__width
                if i + 1 != self.height:
                    string += '\n'
        return string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle" + '.' + '.' + '.')
