#!/usr/bin/python3
"""
8-base_geometry module
create base class and define rectangle object
"""


class BaseGeometry():
    """ Create BaseGeometry class"""

    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validate the value"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Inherited from BaseGeometry class"""
    def __init__(self, width, height):
        """Instantiation for width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
