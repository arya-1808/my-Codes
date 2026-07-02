class pro:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def show(self):
        return f"{self.name}\t {self.price}"
        