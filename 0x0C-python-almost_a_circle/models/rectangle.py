#!/usr/bin/python3\
""" The class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ The class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """ Returns the area of the Rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints the Rectangle in stdout """
        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print('{}{}'.format(' ' * self.__x, '#' * self.__width))

    def __str__(self):
        """ Return a string representation """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        attri = ['id', 'width', 'height', 'x', 'y']

        if args and args[0]:
            for i in range(len(args)):
                setattr(self, attri[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ Return a dictionary representation """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
