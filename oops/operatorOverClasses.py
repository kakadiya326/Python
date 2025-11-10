#Operator Overloading with Two class
class A:
    def __init__(s,a,b):
        s.a=a
        s.b=b
    def display(s):
        print(s.a,s.b)
    def __add__(s,o):
        return A(s.a+o.a,s.b+o.b)
class B:
    def __init__(s,a,b):
        s.a=a
        s.b=b
    def display(s):
        print(s.a,s.b)
    # def __add__(s,o):
    #     return A(s.a+o.a,s.b+o.b)
obj1=A(5,7)
obj2=B(12,8)
obj3=obj1+obj2
obj3.display()