x={}
"""key=input("Enter the key: ")
value=input("Enter the value: ")
x[key]=value
print(x)"""

"""x.update({"name": "Ram"})
x.update({"name": "Shyam"})
x.update({'age':253})
print(x)"""

"""stud={"name":"ram","age":20,"div":"A"}
print(stud.keys())
print(stud.values())
print(stud.items())
for i,j in stud.items():
    print(i,j)"""

'''stud={"name":"ram","age":20,"div":"A","marks":[100,56,78],"sub":["math",'eng'],'rollno':21}
for i in stud.values():
    if type(i)==list:
        for j in i:
            print(j)
        continue
    print(i)'''

product={101:{"product_name":"car","price":1000,"color":"black","qty":10,"model":[501,502]}}
for i in product.values():
    for j in i.items():
        print(j)



    




