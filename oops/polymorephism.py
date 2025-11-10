#Python doesn't support method overloading directly we can achieve by using defualt, variable length argument.
class A:
    def fun(s,a=5,b=6):
        print(a,b)
    def fun1(s,*v):
        print(v)
obj=A()
obj.fun(20,20)
obj.fun1(2,3,4,6,7,8,9,0,2,3,2,3,2,3,2)