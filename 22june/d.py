from b import B
from c import C
class D(B,C):
    def mno(self):
        print("from A class(mno)")
    def __init__(self,name,age,Div,Clg):
        B.__init__(self,name,age)
        C.__init__(self,name,Div)
       
        self.Clg=Clg
        print(f"Collage Name: {self.Clg}")


d=D("Aryaa",'20','A',"PCP")
        