class Com:
    def __init__(self,com_name,com_add):
        self.com_name=com_name
        self.com_add=com_add
    def dis(self):
        print("--------MultiLevel Inhertiance---------")
        print("** Company-->Employee-->Salary")

        return f"Company Name:{self.com_name}\nCompany Address:{self.com_add}"
class Emp(Com):
    def __init__(self, com_name, com_add,emp_id,emp_name):
        super().__init__(com_name, com_add)
        self.emp_id=emp_id
        self.emp_name=emp_name
    def show(self):
        return f"Employee ID:{self.emp_id}\nEmployee Name:{self.emp_name}"
    
class Sal(Emp):
    def __init__(self, com_name, com_add, emp_id, emp_name,bsal):
        super().__init__(com_name, com_add, emp_id, emp_name)
        self.bsal=bsal
    def s(self):
        return f"Salary:{self.bsal}"
    
# s=Sal("Tata",'Pune',101,'Mahesh',35000)
# print(s.dis())
# print(s.show())
# print(s.s())
    
        