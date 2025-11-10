#To define private data member its should start __ (double underscore)
#Private data member can't be accessed directly outside the class.
class A:
    def __init__(s,a,b):
        s.__a=a
        s.__b=b
    def getA(s):
        return s.__a
    def getB(s):
        return s.__b
obj=A(12,40)
print(obj.getA())
print(obj.getB())