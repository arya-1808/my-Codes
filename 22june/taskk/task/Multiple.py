class Acc:
    def __init__(self,bank_name,acc_no):
        self.bank_name=bank_name
        self.acc_no=acc_no
    def show(self):
        print("----------Multiple Inheritance---------")
        print("** Account + Loan-->Customer")
        return f"Bank Name:{self.bank_name}\n Account_no.:{self.acc_no}"
       

class Loan:
    def __init__(self,loan_type,loan_amt):
        self.loan_type=loan_type
        self.loan_amt=loan_amt
    def show1(self):
        return f"Loan_type:{self.loan_type}\n Loan Amount:{self.loan_amt}"
    
class Cust(Acc,Loan):
    def __init__(self, bank_name, acc_no,loan_type,loan_amt,Custid,mobile_no):
        Acc.__init__(self,bank_name, acc_no)
        Loan.__init__(self,loan_type,loan_amt)
        self.Custid=Custid
        self.mobile_no=mobile_no
    def display(self):
        return f"Customer Id:{self.Custid} \n Mobile no.:{self.mobile_no}"

# obj1=Cust("HDFC",'XXXXX5619','Gold Loan','20,00000','109','XXXXXX4419')
# print(obj1.show())
# print(obj1.show1())
# print(obj1.display())

        

        
    