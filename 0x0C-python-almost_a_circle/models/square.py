#!/usr/bin/python3
"""  The class Square that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """ Return a string representation of this Square """
        return ('[Square] ({}) {}/{} - {}'
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Updates the square attributes """
        attri = ['id', 'size', 'x', 'y']

        if args and args[0]:
            for i in range(len(args)):
                setattr(self, attri[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ Return a dictionary representation """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
