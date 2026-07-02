from abc import ABC,abstractmethod
class login(ABC):
    @abstractmethod
    def auth(self):
        pass

class User(login):
    def __init__(self,username,pwd):
        self.username=username
        self.pwd=pwd

    def auth(self,username,pwd):
        if self.username==username and self.pwd==pwd:
             return "Login Successfull !!!"
        else:
            return "Invalid credential"
        
class Admin(login):
    def __init__(self,email,pwd):
        self.email=email
        self.pwd=pwd
    def auth(self,email,pwd):
        if self.email==email and self.pwd==pwd:
             return "Login Successfull !!!"
        else:
            return "Invalid credential"
        
u=User("admin",1234)
print(u.auth("admin",'123'))

    
a=Admin("xyz123@email.com","admin0001")
print(a.auth("xyz123@email.com","admin0001"))
    

