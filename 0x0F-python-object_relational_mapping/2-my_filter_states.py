#!/usr/bin/python3
"""a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()

    # HERE I have to know SQL to grab all states in my database
    cur.execute(
        """SELECT states.id, name
        FROM states
        WHERE name='{:s}'
        ORDER BY id ASC;""".format(state))

    query_rows = cur.fetchall()

    for row in query_rows:
        if row[1] == state:
            print(row)
    cur.close()
    conn.close()
