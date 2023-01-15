#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''This module defines an empty class Rectangle'''


class Rectangle():
    '''define a rectangle class'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''return the value of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the value of width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
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
