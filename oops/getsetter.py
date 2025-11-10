#Getter and Setter using class
class demo:
    def setA(s,x):
        s.a=x
    def setB(s,y):
        s.b=y
    def getA(s):
        print(s.a)
    def getB(s):
        print(s.b)
    def display(s):
        print(s.a,s.b)
ob1=demo()
ob1.setA(12)
ob1.setB(12)
ob1.display()

ob2=demo()
ob2.setA(120)
ob2.setB(52)
ob2.display()