#has a = two different class:car has enginee
#is a= an class have sutype-dog is animal

class Animal:
    type="animal type"
    def __init__(self):
        print("default animal")
    def __init__(self, name,weight):
        self.name=name
        self.weight=weight
    def xyz(self):
        print("Hello im from parent class")
    def greet(self):
        print("hello in animal")