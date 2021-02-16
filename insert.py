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
def insertfunction(Eusername, Epost):
    
    "INSERT INTO blog_post(username, content) VALUES (?, ?)", [Eusername, Epost]
    return