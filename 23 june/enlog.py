import random as rd
import time as tm
class abc:

    def verify(self,u):
        if self.o==u and self.time():
            print("OTP matched")
        else:
            print("Inavalid OTP")

    def __init__(self,name,username,pwd):
        self.name=name
        self.username=username
        self.__pwd=pwd
        
    def login(self,username,pwd):
        if self.username==username and self.__pwd==pwd:
            print("Successfully Login")
            self.o= rd.randint(1000,9999)
            print("OTP is Generated:",self.o)
            u=int(input("Enter the OTP:"))  
            self.verify(u)  
        else:
            print("Invalid Creditals")

obj=abc("ram",'ram@123',1234)
obj.login("ram@123",1234)



  

    