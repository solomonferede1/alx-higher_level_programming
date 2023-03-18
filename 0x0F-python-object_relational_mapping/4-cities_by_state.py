#!/usr/bin/python3
"""
The 4-cities_by_state module
It lists all cities from the database hbtn_0e_4_usa
script should take 3 arguments: mysql username, mysql password and database name
"""

import MySQLdb
import sys


def _Cities():
    """List all cities in the database"""
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id cities.name states.name FROM cities INNER\
     JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    rows = curl.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    _Cities()
