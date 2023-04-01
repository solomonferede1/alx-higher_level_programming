#!/usr/bin/python3
"""
the 6-peak module
Determine the peak from unsorted list
"""


def find_peak(list_of_integers):
    """Finding the peak"""

    if list_of_integers:
        list_of_integers.sort()
        return (list_of_integers[-1])
    return


if __name__ == "__main__":
    find_peak
