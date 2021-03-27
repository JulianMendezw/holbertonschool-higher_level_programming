#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa"""
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
        """SELECT c.name
        FROM cities as c
        JOIN states as s ON c.state_id=s.id
        WHERE s.name = '{:s}'
        ORDER BY c.id ASC;""".format(state,))

    query_rows = cur.fetchall()

    for i in range(len(query_rows)):
        print(query_rows[i][0], end="")
        try:
            if query_rows[i + 1] is not None:
                print(', ', end="")
        except:
                print()

    cur.close()
    conn.close()
