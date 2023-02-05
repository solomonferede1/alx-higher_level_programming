#!/usr/bin/python3
"""
1-my_list module
contains a function that prints the sorted list
"""


class MyList(list):
    """ a class tat inherited from list class and define an instance method
    that prints sorted list:"""

    def print_sorted(self):
        """ prints the list in sorted"""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
