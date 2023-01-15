#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''rectangle module define a class Rectangle and will assign
value foe the width and height of a rectangle'''


class Rectangle:
    '''Defination of a rectangle class'''

    def __init__(self, width=0, height=0):
        '''Method for optiona instantiation of height and width'''

        self.width = width
        self.height = height

    @property
    def width(self):
        '''An instance method that retrieves the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the values of the rectangle'''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''return the value of width'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the value of width'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''Determine and return the area of a rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Determine the perimeter of the rectangle and return'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.width + self.__height))
