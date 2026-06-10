x=set()
print(x,type(x))
x.add(10)
print(x)

x={10,20,30,40,50}
print(x)

x1=list(x)
print(x1[0])

a={1,2,3}
b={3,4,5}
print(a|b)#union
print(a&b)#intersection
print(a-b)#difference
print(a^b)#symmetric difference