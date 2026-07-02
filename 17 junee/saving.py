from ac import Ac
class Saving(Ac):
    def __init__(self,name,add, a_no,bal):
        super().__init__(name,add,a_no)
        self.bal=bal

s=Saving("IDFC","Bhoasri",5690,"10000")
print(s.name)
print(s.add)
print(s.a_no,s.bal)