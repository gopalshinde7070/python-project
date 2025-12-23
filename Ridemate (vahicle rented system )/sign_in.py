class Sign_in:
    def __init__(self,uid="",pas="",name="",age=0,mobile="",address={}):
        self.uid=uid
        self.pas=pas
        self.name=name
        self.age=age
        self.mobile=mobile
        self.address=address
    def __str__(self):
        return f"{self.uid},{self.pas},{self.name},{self.age},{self.mobile},{self.address}"


    
        