class A:
    def xyz(self):
        print("from A class(xyz)")
    def __init__(self,name):
        self.name=name
        print( f"Name: {self.name}")