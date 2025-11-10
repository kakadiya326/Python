#Simple Inheritance
class A:
    def disp(s):
        print("Class A method")
class B(A):
    def disp1(s):
        print("Class B method")
obj=B()
obj.disp()
obj.disp1()