
print("------Hybrid Inheritance------")
class A:
    def __init__(self,name):
        self.name=name
        print( f"Name: {self.name}")


class B(A):
        
    def __init__(self, name,age):
        A.__init__(self,name)
        self.age=age
        print(f"Age:{self.age}")

class C(A):
    
    def __init__(self,name,Div):
        A.__init__(self,name)
        self.Div=Div
        print(f"Division:{self.Div}")

class D(B,C):
    def mno(self):
        print("from A class(mno)")
    def __init__(self,name,age,Div,Clg):
        B.__init__(self,name,age)
        C.__init__(self,name,Div)
       
        self.Clg=Clg
        print(f"Collage Name: {self.Clg}")


d=D("Aryaa",'20','A',"PCP")
        

