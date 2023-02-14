#!/usr/bin/python3
"""
6-base_geometry module
create base class
"""


class BaseGeometry:
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
