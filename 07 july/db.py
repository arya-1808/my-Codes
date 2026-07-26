import mysql.connector

def connection():
    conn = mysql.connector.connect(
    host  = "localhost",
    username = "root",
    password = "arya2008",
    database = "linkcode"
)

print("db connected!")