#Display nearest prime number for the given number.
def isPrime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
n=int(input())
while True:
    if isPrime(n):
        print(n)
        break
    else:
        n=n+1