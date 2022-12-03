#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv) - 1
    if length == 0:
        print("{} {}.".format(length, "arguments"))
    elif length == 1:
        print("{} {}:".format(length, "argument"))
    else:
        print("{} {}:".format(length, "arguments"))
    for i in range(1, length + 1):
        print("{}: {} ".format(i, sys.argv[i]))
