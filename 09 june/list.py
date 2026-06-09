a=((1,"virat",98),(2,"rohit",100),(3,"vaibhav",99),(4,"Mahi",101))
print(a,type(a))
a1=list(a)
#max score 
for i in a1:
    if i[2]==max(a1)[2]:
        print("Max score:",i[1],i[2])

#top 3 players
a1.sort(reverse=True)
for n in a1:
    if n[2]>98:
        print(n[1],n[2])

#total score
total=0
for k in a1:
    total+=k[2]
print("Total score:",total)
