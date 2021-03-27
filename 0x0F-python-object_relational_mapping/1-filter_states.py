#!/usr/bin/python3
"""A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()

    # HERE I have to know SQL to grab all states in my database
    cur.execute(
        "SELECT * FROM states WHERE name RLIKE '^[N]' ORDER BY id ASC;")
    query_rows = cur.fetchall()

    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    conn.close()
