#Initializing both parent have constructor if constructors are there.
class A:
    def __init__(s,u,v):
        s.u=u
        s.v=v
    def display(s):
        print(s.u,s.v,end=" ")
        # B.display(s)
        super().display()
class B:
    def __init__(s,w,x):
        s.w=w
        s.x=x
    def display(s):
        print(s.w,s.x)
class C(A,B):
    def __init__(s, u, v, w, x):
        A.__init__(s,u,v)
        B.__init__(s,w,x)
    def display(s):
        super().display()
obj=C(5,7,8,12)
obj.display()