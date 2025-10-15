#If you pass immutable objects as argument modification did on formal
# parameter doesn't reflect to actual parameter.
def fun(x,y):
    x=x+5
    y=y-1
    print(x,y)
a=10
b=20
fun(a,b)
print(a,b)