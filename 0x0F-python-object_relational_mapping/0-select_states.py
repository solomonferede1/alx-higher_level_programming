#!/usr/bin/python3

"""
The 0-select states module

"""


import MySQLdb
import sys


db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id")
States = cur.fetchall()
for state in States:
    print(state)
cur.close()
db.close()
