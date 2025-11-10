#Initializing parent class constructor
class A:
    def __init__(self,a,b):
        self.a=a 
        self.b=b
    def display(self):
        print(self.a,self.b)
class B(A):
    def display(self):
        print(self.b,self.a)

obj1=B(6,9)
obj1.display()