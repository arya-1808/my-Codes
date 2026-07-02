class hos:
    def __init__(self,hos_name,hos_add):
        self.hos_name=hos_name
        self.hos_add=hos_add
    def w(self):
        return("-----Hierarchical Inheritance-----\n Hospital--->Doctor\n Hospital--->Labs")
    
    def show(self):
       
        return f"Hospital Name:{self.hos_name}\n Hospital Address:{self.hos_add}"
class lab(hos):
    def __init__(self, hos_name, hos_add,lab_id,lab_name):
        super().__init__(hos_name, hos_add)
        self.lab_id=lab_id
        self.lab_name=lab_name
    def dis(self):
        return f"Lab ID:{self.lab_id}\n Lab Name:{self.lab_name}"
    
class doc(hos):
    def __init__(self, hos_name, hos_add,doc_name,specalization):
        super().__init__(hos_name, hos_add)
        self.doc_name=doc_name
        self.specalization=specalization
    def display(self):
        return f"Doctor Name:{self.doc_name}\n Specalization:{self.specalization}"
    
# d=doc("City Hospital","Mumbai","Dr.Kinge","MBBS")
# print(d.w())
# print("---Child Class1----- ")
# print(d.show())
# print(d.display())

# l=lab("K.K.Hospital",'Alandi',1012,'blood lab')
# print("---Child Class2----- ")
# print(l.show())
# print(l.dis())


    
        