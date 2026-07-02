class Acc:
    def __init__(self,bal):
        self.__bal=bal
    def __dep(self):
        amt=int(input("Enter amount to deposite:"))
        self.__bal+=amt
        return f"Total Bal:{self.__bal}"
    
    def get_dep(self):
        return self.__dep()
    
    def __withdraw(self):
        a=int(input("Enter amount to Withdraw:"))
        if self.__bal >=a:
            self.__bal-=a
            return f"Withdrawal Amount:{a} \n Balance:{self.__bal}"
        else:
            return f"Limit Reached"
        
    def get_w(self):
        return self.__withdraw()
obj=Acc(500)
print(obj.get_dep())
print(obj.get_w())

        