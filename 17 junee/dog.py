from animal import Animal
class Dog(Animal):
    def __init__(self):
        print("Child Constructor")
        
    def __init__(self, name, weight,color):
        
        super().__init__(name, weight)
        self.color=color
    def abc(self):
        print("I m from Child Class")

    def detail(self):
        super().greet()
        print(f"{self.name},{self.color}")

    
obj=Dog("Golden Retriver","40kg","Golden")
print(obj.type)
print(obj.name,obj.weight,obj.xyz())

        
