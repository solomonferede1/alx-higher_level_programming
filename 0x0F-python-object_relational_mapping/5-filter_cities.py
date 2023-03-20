#!/usr/bin/python3
"""
The 5-filter_cities.py module
It is a script that takes in the name of a state as an argument and
lists all cities of that state, using the database
script should take 4 arguments: mysql username, mysql password
and database name
"""

import MySQLdb
import sys


def _Cities():
    """List all cities in the database"""
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON\
    cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id", (sys.argv[4], ))
    rows = cur.fetchall()
    city_list = []
    for row in rows:
        city_list.append(row[0])
    print(', '.join(city_list))
    cur.close()
    db.close()


if __name__ == "__main__":
    _Cities()
