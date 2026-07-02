from bank import Bank
class Ac(Bank):
    def __init__(self,name,add,a_no):
        super().__init__(name,add)
        self.a_no=a_no