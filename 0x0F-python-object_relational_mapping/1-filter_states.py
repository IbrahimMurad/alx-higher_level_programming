#!/usr/bin/python3

"""This script ists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
the user is passed as the first argument,
the passowrd is passed as the second argument and
the database name is passed as the third argument.

"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
