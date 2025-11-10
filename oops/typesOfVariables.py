#Instance and class variables
class demo:
    c=10
    def __init__(s,a,b):
        s.a=a
        s.b=b
    def display(s):
        print(s.a,s.b,s.c,demo.c)
obj=demo(2,3)