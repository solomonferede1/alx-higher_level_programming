#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''this module defines a square by: (based on 1-square.py)

    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError exception with
    the message size must be an integer
    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0
    '''


class Square:
    '''A Square class that defines a square and initialize
    the size attribute'''
    def __init__(self, size=0):
        '''Initialize the size of a square

        Args:
            size(int): Size of the square

        '''
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
