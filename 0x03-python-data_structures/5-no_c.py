#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for ch in range(len(my_string)):
        if ch == 'c' or ch == 'C':
            new_string += ch
    return (new_string)
