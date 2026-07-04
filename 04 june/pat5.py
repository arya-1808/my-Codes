l1=[1,3,5,3,1]

for i in l1:
    s=(5-i)//2

    if i==1:
        print("."*s + "1"*1)

    elif i==3:
        print("."*s + "3"*3)

    else:
        print("."*s + "5"*5)
