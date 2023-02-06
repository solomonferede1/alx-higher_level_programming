#!/usr/bin/python3
"""
The rectangle module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """the Square class inherites from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initailize the private attribute"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''getter method for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter method for size'''
        self.width = value
        self.height = value

    def __str__(self):
        '''overwriten the __str__ method that inherint from Rectangle'''

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)
