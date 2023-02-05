#!/usr/bin/python3
# Solomon
"""
1-my_list module
contains a function that prints the sorted list
"""


class MyList(list):
    """ a class that inherited from list class and define an instance method
    that prints sorted list:"""

    def print_sorted(self):
        """ prints the list in sorted"""
        print(sorted(self))
