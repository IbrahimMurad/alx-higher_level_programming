#!/usr/bin/python3
""" In this module, we define Square class
that inherits from Rectangle class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class inherits from Rectangle class
    as a special cass of a rectangle where
    its height equals its width which is called size """

    @property
    def size(self):
        """ size getter """

        return self.width

    @size.setter
    def size(self, size):
        """ size setter """

        self.width = size
        self.height = size

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes size, x, y and id """

        size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns a string representing the data in the class """

        my_str = "[Square] ({}) {}/".format(self.id, self.x)
        my_str += "{} - {}".format(self.y, self.size)
        return my_str

    def update(self, *args, **kwargs):
        """ updates the attribut's values """

        args_len = len(args)
        if args_len == 0:
            if 'id' in kwargs.keys():
                self.id = kwargs['id']
            if 'size' in kwargs.keys():
                self.size = kwargs['size']
            if 'x' in kwargs.keys():
                self.x = kwargs['x']
            if 'y' in kwargs.keys():
                self.y = kwargs['y']
        else:
            if args_len > 0:
                self.id = args[0]
            if args_len > 1:
                self.size = args[1]
            if args_len > 2:
                self.x = args[2]
            if args_len > 3:
                self.y = args[3]

    def to_dictionary(self):
        """  returns the dictionary representation of a Square """
        
        my_dict = {'id': self.id, 'size': self.size}
        my_dict.update({'x': self.x, 'y':self.y})
        return my_dict