#If both parent & child class having same method, child class method
# overrides functionality of parent class it is called method overring.
class A:
    def disp(s):
        print('Class A method')
class B(A):
    def disp(s):
        print('Class B method')
obj=B()
obj.disp()