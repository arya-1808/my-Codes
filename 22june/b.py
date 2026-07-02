from a import A
class B(A):
    # def abc(self):
    #     print("from A class(abc)")

    def __init__(self, name,age):
        A.__init__(self,name)
        self.age=age
        print(f"Age:{self.age}")