#exception zero
"""print('start')
try:
    print(10/0)
except:
    print("division by Zero")
print('end')"""
#enter a char
"""try:
    a=int(input("Enter a no"))
except:
    print(" only numbersare allowed ")"""
# both in one
try:
    a=int(input("Enter a no:"))
    a1=int(input("Enter a no:"))
    print(a/a1)
except Exception as e:
    print(e)
except ValueError as h:
    print(h)


