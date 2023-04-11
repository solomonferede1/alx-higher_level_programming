#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''this module defines a square by: (based on 1-square.py)

    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError exception with
    the message size must be an integer
    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0

    It also determine the area of the square
    '''


class Square:
    '''A Square class that defines a square and initialize
    the size attribute'''
    def __init__(self, size=0):
        '''Initialize the size of a square

        Args:
            size(int): Size of the square

        '''
        self.size = size

    @property
    def size(self):
        '''A method that retrieve the size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Set the valid value of the size attribute'''
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        '''Determine the area of a square and return it'''
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
