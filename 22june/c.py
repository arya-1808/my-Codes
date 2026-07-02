from a import A
class C(A):
    def pqr(self):
        print("from A class(pqr)")

    def __init__(self,name,Div):
        A.__init__(self,name)
        self.Div=Div
        print(f"Division:{self.Div}")