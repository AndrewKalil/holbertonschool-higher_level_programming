#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Inherited class from Base class - Rectangle

    Args:
        Base (class): the base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation of new object

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int, optional): x parameter. Defaults to 0.
            y (int, optional): y parameter. Defaults to 0.
            id (int, optional): id of object. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """property setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ sets value of width

        Args:
            value (int): value to be set
        """
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """property setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets value for height

        Args:
            value (int): value to be set
        """
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """property setter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ sets value of x

        Args:
            value (int): value to be set
        """
        self.integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """property setter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ sets value for y

        Args:
            value (int): value to be set
        """
        self.integer_validator('y', value)
        self.__y = value

    def integer_validator(self, name, value):
        """Integer validator

        Arguments:
            name {string} -- name of value to be validated
            value {int} -- value to be validated

        Raises:
            TypeError: <name of attribute> must be an integer
            ValueError: <name of attribute> must be > 0
            ValueError: <name of attribute> must be >= 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if (name is "width" or name is "height") and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        if (name is "x" or name is "y") and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        """area of the rectangle

        Returns:
            int: result for area of the reactangle object
        """
        return self.width * self.height

    def display(self):
        """prints rectangle with '#'
        """
        if self.y > 0:
            print("\n"*self.y, end="")
        for i in range(self.height):
            print("{}{}".format(" "*self.x, "#"*self.width))

    def __str__(self):
        """string containging information aboutt the triangle

        Returns:
            str: string description
        """
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
        return string

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
                    self.width = i
                elif cnt is 3:
                    self.height = i
                elif cnt is 4:
                    self.x = i
                elif cnt is 5:
                    self.y = i
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """turns attributes to a dictionary

        Returns:
            dict: dictionary with all attributes
        """
        dic = {}
        ls = ['id', 'width', 'height', 'x', 'y']
        for i in ls:
            dic[i] = getattr(self, i)
        return dic
