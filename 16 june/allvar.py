global_var="hey"
class demo:
    pass
    msg='Hello'

    def __init__(self):
        print("Created")
    def __init__(self,age):
        self.name="abc"
        self.age=age
    def __del__(self):
        print("Deleted")
    def access(self):
        print(global_var)
        local_var=90
        return local_var
        

obj=demo(20)
print(obj.name)
print(obj.age)
print(obj.msg)
print(obj.access())

        
    
