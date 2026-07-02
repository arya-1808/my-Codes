from p1 import p1
from p2 import p2
class ch(p1,p2):
    def xyz(self):
        print('Child class')
    def call_p2(self):
        return  p2.show(self)
    def __init__(self, name,age):
        print("Child Constructor")
        p1.__init__(self,name)
        p2.__init__(self,age)
        
    
obj=ch("ram",20)
# obj.abc()
# obj.pqr()
# obj.xyz()
# obj.show()
# obj.call_p2()
 