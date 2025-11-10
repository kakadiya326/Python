# Count the number of objects created from a class
class A:
    c=0
    def __init__(s):
        A.c=A.c+1
    @staticmethod
    def disp():
        print(A.c)
obj1=A()
obj2=A()
obj3=A()
obj4=A()
obj5=A()
A.disp()