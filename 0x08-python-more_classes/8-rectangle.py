#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''rectangle module define a class Rectangle and will assign
value foe the width and height of a rectangle'''


class Rectangle:
    '''Defination of a rectangle class'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Method for optiona instantiation of height and width'''

        Rectangle.number_of_instances += 1
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

    def __str__(self):
        '''Retur the string representation of the object'''

        string = ''
        if self.__width == 0:
            return string
        for i in range(self.__height):
            string += (self.__width * str(self.print_symbol))
            if i != self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        '''Return the internal representation of an object parsed by pyton'''
        return "Rectangle(" + str(self.width) + ', ' + str(self.height) + ")"

    def __del__(self):
        """ Delete the instance of a rectangle"""
        print("Bye rectangle...")
        del self
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Return the biggest rectangle based on the area"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.width * rect_1.height
        area2 = rect_2.width * rect_2.height
        if area1 == area2:
            return rect_1
        elif area1 > area2:
            return rect_1
        else:
            return rect_2
