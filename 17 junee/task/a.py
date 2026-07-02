from Bank import B
class A(B):
    def __init__(self,bname,ifsc,acc_no,acc_name):
        super().__init__(bname,ifsc)
        self.acc_no=acc_no
        self.acc_name=acc_name
    def show2(self):
        super().show1()
        return f"Account_no: {self.acc_no} Account_name: {self.acc_name}"