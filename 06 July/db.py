import mysql.connector as x

def get_connection():
    conn = x.connect(
        host = "localhost",
        username = "root",
        password = "arya2008",
        database = "linkcode"
        )
    print("databse connected!")
    return conn
get_connection()