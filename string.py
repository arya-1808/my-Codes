str1="Maharashtra"
even=0
odd=0
for i in range(len(str1)):
    if(i%2==0):
        even+=1
    else:
        odd+=1
    
print(even)
print(odd)