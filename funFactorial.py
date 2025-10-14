#Define a factorial() function to return factorial of a given number.
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
print(fact(5))