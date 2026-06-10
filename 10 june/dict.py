x={}
print(x,type(x))
#add
x={"name": "Ram"}
print(x)
#update
x["name"]="Shyam"
print(x)
x[101]='Stud data'
print(x)
#del and pop
del x[101]
print(x)

x.pop("name")
print(x)