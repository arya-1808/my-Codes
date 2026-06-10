from unicodedata import name


stud={101:{"name":"ram","age":18,"sub":("python","mern","java"),"marks":[30,59,78]},
      102:{"name":"sita","age":18,"sub":("python","mern","java"),"marks":[70,80,90]},
      103:{"name":"gita","age":21,"sub":("python","mern","java"),"marks":[89,90,100]},
      104:{"name":"rahul","age":19,"sub":("python","mern","java"),"marks":[88,97,100]}
     }
# display name and total marks of all students
"""for i, m in stud.items():
    sum = 0
    for j in m["marks"]:
        sum += j

    print(i, end=" ")
    print(m["name"], end=" ")
    print(sum)"""
#displaying the topper
"""top = 0
for i, m in stud.items():
    sum = 0
    for j in m["marks"]:
        sum += j
if sum >top:
    top=sum
    name=m["name"]
print(i,end=" ")
print(name,top)"""
       
#highest marks in python
"""a=0
for i in stud.values():
    if i["marks"][0]>a:
        a=i["marks"][0]
      
print(i["name"],end=" ")
print(a)"""

#greater than 70 and less than 90 in mern
for i in stud.values():
    if i["marks"][1]>70 and i["marks"][1]<90:
        print(i["name"],end=" ")
        print(i["marks"][1])

# age greaterthan 19
for i in stud.values():
    if i["age"]>19:
        print(i["name"],end=" ")
        print(i["age"])
      

