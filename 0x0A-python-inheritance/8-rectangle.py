#!/usr/bin/python3
"""
8-base_geometry module
create base class and define rectangle object
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherited from BaseGeometry class"""
    def __init__(self, width, height):
        """Instantiation for width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
