#!/usr/bin/python3

""" This script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    query_statement = "SELECT * FROM states\
 WHERE states.name = '{}'".format(sys.argv[4])
    cur.execute(query_statement)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
