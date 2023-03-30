#!/usr/bin/python3

"""
The 2-filter states module

"""


import MySQLdb
import sys


def _States():
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id".
                format(sys.argv[4]))
    States = cur.fetchall()
    for state in States:
        if (state[1] == sys.argv[4]):
            print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    _States()
