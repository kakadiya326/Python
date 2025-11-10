#Multiple Inheritance: MRO( Method Resolution Orders)
class A:
    def m1(s):
        print("M1 EXE")
class B:
    def m2(s):
        print("M2 EXE")
class C(A,B):
    def m3(s):
        print("M3 EXE")
obj=C()
obj.m1()
obj.m2()
obj.m3()

class X:
    def disp(s):
        print("M1")
        super().disp()
class Y:
    def disp(s):
        print("M2")
class Z(X,Y):
    def disp(s):
        print("M3")
        super().disp()
obj=Z()
obj.disp()