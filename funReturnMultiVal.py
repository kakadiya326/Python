#Return multiple values from a function
def fun():
    x=5
    y=10
    z=25
    t=1
    return x,y,z,t
print(fun())    #(5, 10, 25, 1)
a,b,c,d=fun()
print(a,b,c,d)  #5 10 25 1
a,*v=fun()  #*v --> return data in list format
print(a,v)  #5 [10, 25, 1]