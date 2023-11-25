#!/usr/bin/pyhton3
""" This scrpit returns a filtered states """

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2], db=argv[3])

        # Create a cursor to execute queries
        cur = db.cursor()

        # Execute the query to retrieve states
        cur.execute(
            """SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER BY id""")

        # Fetch all the rows and print the results
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
