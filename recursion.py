#using recursion factorial.
def facto(n):
    if n==1:
        return 1
    else:
        return n*facto(n-1)
print(facto(5))

#Sum of indivisual digits in number.
def fun(n):
    if n<10:
        return n
    else:
        return n%10+fun(n//10)
print(fun(46))

#Sum of list element
def sumList(l,i):
    if i == len(l):
        return 0
    else:
        return l[i]+sumList(l,i+1)
l=[3,5,3,5,7,8]
print(sum(l,0))

#Implement GCD using Recursion
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(12,18))

#Calculate nth term in Fibonacci sequence.
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(5))

#Implement binary search using recursion.
def bs(a,k,l,u):
    if l<=u:
        m=(l+u)//2
        if a[m]==k:
            return m
        elif k<a[m]:
            return bs(a,k,l,m-1)
        else:
            return bs(a,k,m+1,u)
    else:
        return -1
a=[2,4,6,7,8,9,10,12,15]
print(bs(a,8,0,len(a)-1))

#Three tower problem.
def toh(n,s,d,a):
    if n==1:
        print(f"Disc-1 moved from {s} to {d} ")
    else:
        toh(n-1,s,a,d)
        print(f"Disc-{n} moved from {s} to {d}")
        toh(n-1, a,d,s)
toh(3,'sc','dt','ax')