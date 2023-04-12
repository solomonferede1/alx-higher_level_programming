#!/usr/bin/python3
"""
100=my_int module
Write a class MyInt that inherits from int:

MyInt is a rebel. MyInt has == and != operators inverted
You are not allowed to import any module
"""


class MyInt(int):
    """MyInt inherited from int"""

    def __init__(self, value):
        self.value = value

    def __eq__(self, object):
        """inverted == implimentation"""
        return (self.value != object)

    def __ne__(self, object):
        """invert not equal implementation"""
        return (self.value == object)
