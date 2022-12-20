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
    def __init__(self, size=0, position=(0, 0)):
        '''Initialize the size  and position of a square

        Args:
            size(int): Size of the square

        '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''A method that retrieve the size of the square'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Set the valid value of the position attribute'''
        if isinstance(value, tuple) and value >= (0, 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''Determine the area of a square and return it'''
        return self.__size ** 2

    def my_print(self):
        '''Prints in stdout the square with the character #'''
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print('\n' * (self.__position[1] - 1))
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print('#' * self.__size)
