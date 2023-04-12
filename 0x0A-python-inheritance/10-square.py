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


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """A Square class inherited from Rectangle"""

    def __init__(self, size):
        """"instantiation of width and height"""
        super(BaseGeometry, self).integer_validator('size', size)
        self.__size = size

    def area(self):
        """Determine the area of rectangle"""
        return (self.__size ** 2)
