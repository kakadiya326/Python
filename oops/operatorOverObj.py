#Define our own functionality to the existing operator by overring appropriate 
# method in our class is called operator overloadin
class A:
    def __init__(s,a,b):
        s.a=a
        s.b=b
    def display(s):
        print(s.a,s.b)
    def __add__(s,o):
        return A(s.a+o.a,s.b+o.b)
obj1=A(5,9)
obj2=A(12,3)
obj3=obj1+obj2
obj3.display() #17 12