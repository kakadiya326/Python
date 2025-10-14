#Variable length keyword arguments
def fun(**kw):
    print(kw)
fun(a=5,b=10,c=15,d=20,e=25)
fun(name='chiranj',age=23,dept='MCA')