#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()
    if rows:
        for i in range(len(rows)):
            string = str(rows[i])
            if i < (len(rows)-1):
                print("{}, ".format(string[2:-3]), end="")
            else:
                print("{}".format(string[2:-3]))
    cur.close()
    db.close()
