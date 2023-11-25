#!/usr/bin/python3
""" This script return filter states """
if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3])
        cur = db.cursor()
        cur.execute("""SELECT * FROM states
                WHERE name LIKE BINARY %s
                ORDER BY id""", (argv[4],))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{:d}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(str(e)))
