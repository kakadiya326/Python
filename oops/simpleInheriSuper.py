#To get the parent class display method also in child super() method will use.
class A:
    def display(s):
        print('Class A method')
class B(A):
    def display(s):
        super().display()
        print('Class B method')
obj1=B()
obj1.display()