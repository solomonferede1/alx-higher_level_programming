#!/usr/bin/python3
"""
The rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """the rectangle class inherited from the base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initailize the private attribute"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieve the value"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the valid value for the private attribute height"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Retrieve the value"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the valid value for the private attribute height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Retrieve the value"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the valid value for the private attribute x"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Retrieve the value"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the valid value for the private attribute x"""
        """Set the valid value for the private attribute x"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character # """
        [print() for space in range(self.y)]
        [print(" " * self.x + "#" * self.width)
         for line in range(self.height)]

    def __repr__(self):
        '''Return the internal representation of an object parsed by pyton'''
        return "[Rectangle] (" + str(self.id) + ') ' + str(self.__x) +\
            "/" + str(self.__y) + ' - ' + str(self.__width) + '/' +\
            str(self.__height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute:"""
        index = 0
        if len(args) > 0 and args:
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.__width = arg
                elif index == 2:
                    self.__height = arg
                elif index == 3:
                    self.__x = arg
                elif index == 4:
                    self.__y = arg
                index += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
