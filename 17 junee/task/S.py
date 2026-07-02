from a import A
class Sa(A):
    def __init__(self,bname,ifsc,acc_no,acc_name,bal,fd):
        super().__init__(bname,ifsc,acc_no,acc_name)
        self.bal=bal
        self.fd=fd
        print(" Org Balance",self.bal)
    def dep(self,amt):
        self.bal+=amt
        print("Balance:",self.bal)
        print("Amount:",amt)

    def wdraw(self,amt):
        if amt <= 2500:
            self.bal-=amt
            print("Current Balance:",self.bal)
        else:
            print("Maximun Reached")

    def f(self,amt,m):
        if m==12:
            a=amt*7/100
        elif m==6:
            a=amt*5/100
    
            
        
        total= amt + a
        print("Fd amount:",amt)
        print("Interest:",a)
        print("Total Amount:",total)

s1=Sa("IDFC","IDFC123546","5619","Geeta",5000,10000)
print(s1.show1())
print(s1.show2())
# s1=Sa("SBI","SBIN0001",12345,"Arya",5000,10000)

s1.dep(1000)

s1.wdraw(1000)

s1.f(10000,12)




        
            


        