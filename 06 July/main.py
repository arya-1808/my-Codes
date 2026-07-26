from crud import *

def login():

    conn = get_connection()
    cursor = conn.cursor()

    username = input("enter your username :")
    password = input("enter your password :")
    cursor.execute("select * from login where username = %s",(username,))
    row = cursor.fetchone()
    print(row[2],row)
    if row [3] =="admin":
        print("1.add user to main\n2.add student\n3.view student\4.exit\n")
        choice = int(input("enter your choice :"))
        match choice:
            case 1: 
                add_user()
            
            case 2:
                add_stud()

            case 3:
                view_stud()

            case 4:
                print("Exit!")

    elif row [3] =="user":
        print("1.view stud")
login()