"""for i in range(6):
    for j in range(6):
        print("*", end="")
    print()"""

#hallow square
"""for i in range(6):
    for j in range(6):
        if i==0 or i==5 or j==0 or j==5:
            print("*", end="")
        else:
            print(" ", end="")
    print()"""

# diamond pattern
for i in range(1,11+1):
    for j in range(1,i+1):
        if i%2!=0:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(12,1,-1):
    for j in range(i+1,1,-1):
        if i%2!=0:
            print("*", end="")
        else:
            print(" ", end="")
    print()
