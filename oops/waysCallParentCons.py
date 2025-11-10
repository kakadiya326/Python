#To call parent class constructor into child class super method or parent class name will use.
#If parent class constructor called through super() self reference will supply automatically.
#If called through class name explicitly we need to supply
class A:
    def __init__(self,a,b):
        self.a=a 
        self.b=b
    def display(self):
        print(self.a,self.b,end=" ")
class B(A):
    def __init__(self, a, b,c,d):
        #super().__init__(a, b) #Don't need to supply self in super()
        A.__init__(self,a,b) #Must to pass self when class name used
        self.c=c
        self.d=d
    def display(self):
        super().display()
        print(self.c,self.d)
obj=B(6,9,19,12)
obj.display()