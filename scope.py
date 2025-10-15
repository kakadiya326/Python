#Local scope
def fun():
    a=10
    print(a)
fun()
# print(a)    #NameError

#Global Scope
def fun():
    print(a)
a=10
fun()
print(a)

#Local and Global scope example
def fun1():
    a=5
    print(a)
a=10
fun1()
print(a)

#To modify global scope varible within local scope, global keyword
def fun2():
    global a
    a=5
    print(a)
a=10
fun2()
print(a)

#To access global variable within local scope global() 
def fun3():
    a=5
    print(a,globals()['a'])
a=10
fun3()
print(a)