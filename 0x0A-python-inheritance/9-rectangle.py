#!/usr/bin/python3
"""
9-rectangle module
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)

Instantiation with width and height: def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following rectangle
description: [Rectangle] <width>/<height>
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class inherited from BaseGeometry"""

    def __init__(self, width, height):
        """"instantiation of width and height"""
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    def area(self):
        """Determine the area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the str representation of Rectangle object"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
