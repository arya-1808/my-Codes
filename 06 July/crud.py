from db import get_connection 
from student import student
from user import user

# entire crud():

def add_stud():
    conn = get_connection()
    cursor = conn.cursor()
    stud_name = input("enter your name :")
    stud_age = int(input("enter your age :"))
    stud_email = input("enter your email id :")
    obj = student(stud_name,stud_age,stud_email)
    query = "insert into student (stud_name,stud_age,stud_email) values(%s,%s,%s)"
    values = (obj.stud_name,obj.stud_age,obj.stud_email)
    cursor.execute(query,values)
    conn.commit()
    print("student addeed!")

# print(add_stud())
def add_user():
    conn = get_connection()
    cursor = conn.cursor()
    username = input("enter your username :")
    password = input("enter your password :")
    role = input("enter your role :")
    obj = user(username,password,role)
    query = "insert into login(username,password,role) values(%s,%s,%s)"
    values = (obj.username,obj.password,obj.role)
    cursor.execute(query,values)
    conn.commit()
    print("added!")

# add_user()

def view_stud():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    return rows
# print(view_stud())