#!/usr/bin/python3
"""
the 6-peak module
Determine the peak from unsorted list
"""


def find_peak(list_of_integers):
    """Finding the peak"""

    if list_of_integers != []:
        for i in range(len(list_of_integers) - 1):
            if list_of_integers[i] > list_of_integers[i + 1]:
                tmp = list_of_integers[i + 1]
                list_of_integers[i + 1] = list_of_integers[i]
                list_of_integers[i] = tmp
        return (list_of_integers[-1])
    return


if __name__ == "__main__":
    find_peak
