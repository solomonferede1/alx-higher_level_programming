#!/usr/bin/python3
# Solomon Ferede - solomonf1227@gmail.com
"""
3-is_kind_of_class module
check wether the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class
"""


def is_kind_of_class(obj, a_class):
    """Function that returns true if an object is an instance of the class"""
    return (isinstance(obj, a_class))
