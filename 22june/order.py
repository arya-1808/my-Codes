from product import pro
from payment import py
class order(pro,py):
    def bill(self):
        q=int(input("Enter a the qty to add:"))
        total=self.price*q
        print('---Bill---')
        print("pro_name Price \t qty")
        print(self.show(),"\t",q)
        print("---------------------")
        print("Total",total)

o1=order("car",500)
o1.bill()