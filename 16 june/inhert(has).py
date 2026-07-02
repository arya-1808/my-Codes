class car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.eng=eng(1234,500)

    def show(self):
        return f"{self.name} {self.price}"
    def show1(self):
        print(self.show())
        print(self.eng.display())



class eng:
    def __init__(self,horsepower,chessno):
        self.horsepower=horsepower
        self.chessno=chessno
    def display(self):
        return f"{self.horsepower},{self.chessno}"
  
    
c=car("BMW",'2cr')
print(c.show())
print(c.name)
print(c.eng.chessno)

c.show1()


        