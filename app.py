import dbcreds
import mariadb
import sys

#1. connect to the DB
def connect():
    return mariadb.connect(
    user = dbcreds.user,
    password = dbcreds.password,
    host = dbcreds.host,
    port = dbcreds.port,
    database = dbcreds.database   
)

def login():
   
    conn = None
    cursor = None
    conn = connect()
    cursor = conn.cursor()
    try:
        print("Welcome to the python blog post site.")
        myusername = input("Enter your username: ")
        mypassword = input("Enter your password: ")

        if myusername != "" and mypassword != "":
            try:
                cursor.execute("SELECT * FROM Users WHERE username=? AND password=? limit 1", [myusername, mypassword]
                )
                result = cursor.fetchall()[0]
                count = cursor.rowcount
                print("row count", count)
                if cursor.rowcount == 1:
                    userId = result[0]
                    name = result[1]
                    pwd = result[2]

                else:
                    ("Something went wrong. Please try again.")
                    pass

            except:
                print("That is not a valid username or password! Please try again.")
                login()

            else:
                pass
        else:
            print("The username and/or password fields cannot be empty. Please try again")

        while True:
            print()
            print("Welcome back " + myusername + " To make a selection enter the corresponding number: ")
            print("1. Make a post")
            print("2. View all posts")

            userselection = int(input("My choice is: "))

            if (userselection > 0 and userselection < 3):                     
                if userselection == 1:
                    print("You chose #1")
                    print("New Posting")
                    username = myusername
                    post = input("Enter your blog post here: ")
                    E_username = username.encode()
                    E_post = post.encode()
                    cursor.execute(
                        "INSERT INTO blog_post(username, content) VALUES (?, ?)", [E_username, E_post]
                    )
                    # commit the change
                    conn.commit()
                
                elif userselection == 2:
                    try:
                    # retrieve data
                        cursor.execute(
                            "SELECT * FROM blog_post"
                        )

                        result = cursor.fetchall()
                        count = cursor.rowcount
                        print(result)
                        print("row count:", count)
                 
                    except:
                        mariadb.DataError()
                        print("There are no saved blog posts.")

                    finally:
                        pass
                                
            else:
                print("Invalid selection. Only integers between 1 and 4 are allowed. Please try again")

    except:
        mariadb.OperationalError()

    finally:
        if (cursor != None):
            cursor.close()
        if (conn != None):
            conn.rollback()
            conn.close()
        
    return result

result = login()

			








