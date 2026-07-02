class Clg:
    def __init__(self,clg_name,clg_add):
        self.clg_name=clg_name
        self.clg_add=clg_add

    def show(self):
        print("--------Single Inheritance--------")
        print("**   Collage ---> Student")
        print(f"Collage Name:{self.clg_name} \n Collage Address:{self.clg_add}")
    
class Stud(Clg):
    def __init__(self, clg_name, clg_add,stud_name,roll_no):
        super().__init__(clg_name, clg_add)
        self.stud_name=stud_name
        self.roll_no=roll_no
    def show1(self):
        print(f"Student Name:{self.stud_name}\n Roll_no:{self.roll_no}")

# obj=Stud("PCP","Akurdi","Sita","101")
# obj.show()
# obj.show1()