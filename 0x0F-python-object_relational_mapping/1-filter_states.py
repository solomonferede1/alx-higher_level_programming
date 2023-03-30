#!/usr/bin/python3
"""
The 1-filter_states module

selsts the states start with n
"""


import MySQLdb
import sys


def _States():
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    rows = cur.fetchall()

    for row in rows:
        if row[1][0] == "N":
            print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    _States()
