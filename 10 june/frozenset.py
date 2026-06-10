x=frozenset([1,3,8])
print(x)
x1=frozenset((4,'arya'))
print(x1)
for i in x:
    print(i)

print(8 in x)
# frozenset is immutable and does not support add,update,remove,discard,pop,clear methods