from Single import Clg,Stud
from Multiple import Acc,Loan,Cust
from Multilevel import Com,Emp,Sal
from hierarchical import hos,lab,doc
from hybrid import A,B,C,D

while True:
    print("\n1.Single Inheritance\n2.Multiple Inheritance \n3.Multilevel Inheritance\n4.Hierarchical Inheritance \n5. Hybrid Inheritance \n6.Exit")
    ip=int(input("Enter Your Choice:"))
    match ip:
        case 1:
            obj=Stud("PCP","Akurdi","Sita","101")
            obj.show()
            obj.show1()

        case 2:
            obj1=Cust("HDFC",'XXXXX5619','Gold Loan','20,00000','109','XXXXXX4419')
            print(obj1.show())
            print(obj1.show1())
            print(obj1.display())

        case 3:
            s=Sal("Tata",'Pune',101,'Mahesh',35000)
            print(s.dis())
            print(s.show())
            print(s.s())

        case 4:
            d=doc("City Hospital","Mumbai","Dr.Kinge","MBBS")
            print(d.w())
            print("---Child Class1----- ")
            print(d.show())
            print(d.display())

            l=lab("K.K.Hospital",'Alandi',1012,'blood lab')
            print("---Child Class2----- ")
            print(l.show())
            print(l.dis())

        case 5:
            d=D("Aryaa",'20','A',"PCP")
        
        case 6:
            print("Thank You !!")

        case _:
            print("Invalid Choice")

    



        

        
              
