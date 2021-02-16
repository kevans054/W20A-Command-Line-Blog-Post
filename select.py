import dbcreds
import mariadb

#1. connect to the DB
conn = mariadb.connect(
    user = dbcreds.user,
    password = dbcreds.password,
    host = dbcreds.host,
    port = dbcreds.port,
    database = dbcreds.database   
)

def select():
    while True:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users"
            )
        row = cursor.fetchone()
        print(row)
        while row is not None:
            if username == username and password == password:
                print(row)
                row = cursor.fetchone()
            else:
                break
        # close the cursor
        cursor.close()
        # close the connection
        conn.close()
        return result
select()