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

def login()
    myusername = input("Enter your username: ")
    mypassword = input("Enter your password: ")
        if myusername != "" and mypassword != "":
            try:
                cursor.execute(
                    "SELECT id, username, password FROM users"
                        )
                    row = cursor.fetchone()
                    print(row)
                    while row is not None:
                    #    if myusername == username and mypassword == password:
                            print(row)
                            row = cursor.fetchone()
                    #    else:
                     #       break
                finally:
                    break
            else:
                print("That is not a valid login. Please try again")