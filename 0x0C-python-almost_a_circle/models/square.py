#!/usr/bin/python3
"""class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """New class Square inherited from Rectangle class

    Args:
        Rectangle (class): class rectangle containing useful attributes
        and methods for Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation on Square obects

        Args:
            size (int): size of square
            x (int, optional): horizontal shift. Defaults to 0.
            y (int, optional): vertical shift. Defaults to 0.
            id (int, optional): id of object. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string containging information about the square

        Returns:
            str: string description
        """
        string = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
        return string

    @property
    def size(self):
        """size of squre

        Returns:
            [type]: [description]
        """        """propetry for size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter

        Args:
            value (int): value to be set
        """
        self.width = value
        self.heigth = value

    def update(self, *args, **kwargs):
        """udates an object
        """
        cnt = 0
        if args is not None and len(args) is not 0:
            for i in args:
                cnt += 1
                if cnt is 1:
                    self.id = i
                elif cnt is 2:
                    self.size = i
                elif cnt is 3:
                    self.x = i
                elif cnt is 4:
                    self.y = i
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """turns attributes to a dictionary

        Returns:
            dict: dictionary of object attributes
        """
        dic = {}
        ls = ['id', 'size', 'x', 'y']
        for i in ls:
            dic[i] = getattr(self, i)
        return dic
