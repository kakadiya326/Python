#Decorators is a function it will take other fucntion 
# as a arguments it will enhance it's functionality 
# it will return update function

#Convert sqr() into cube using decorator().
def decoFun(fun):
    def updated(n):
        return fun(n)*n
    return updated
@decoFun
def sqr(n):
    return n*n
print(sqr(6))

#Convert a+b into a+b**3 using decorator function.
def decFun(fun):
    def uptFun(a,b):
        return fun(a,b)**3
    return uptFun
@decFun
def add(a,b):
    return a+b
print(add(3,5))