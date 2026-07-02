from abc import ABC,abstractmethod
class xyz(ABC):
     
    def xyz(self):
          print("hello xyz")
    @abstractmethod
    def show(self):
         pass
         
class pqr(xyz):
     def show(self):
          print("I am from Child class")
     
obj=pqr()
obj.xyz()
obj.show()