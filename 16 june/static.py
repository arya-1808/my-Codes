class demo:
    msg="Hello"
    @classmethod
    def d(cls):
        return cls.msg
    def __init__(self,age):
        self.name="abc"
        self.age=age
    def dis(self):
        print("name is",self.name,end=",")
        print("age is",self.age)

    @staticmethod
    def greet(name,objref):
        return f"hello gm {name} {demo.msg} {objref.age}"
    
obj=demo(20)
obj.dis()
#1 way of calling class method
print(obj.d())
#2 way of calling class method
print(demo.d())
#1 way of calling static method
print(obj.greet("Sita",obj))
#2 way of calling static method
print(demo.greet("Geeta",obj))

    
    