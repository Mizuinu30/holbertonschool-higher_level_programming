#!/usr/bin/python3
""" This script return filter cities """

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
        cur.execute("""SELECT cities.name
                    FROM cities
                    INNER JOIN states
                    ON cities.state_id = states.id
                    WHERE states.name LIKE BINARY %s
                    ORDER BY cities.id""", (argv[4],))
        rows = cur.fetchall()
        print(", ".join([row[0] for row in rows]))
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{:d}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(str(e)))
