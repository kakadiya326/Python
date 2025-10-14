#Display nearest Prime and Palindrome number.
def isPrime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    
def isPalin(s):
    n=str(s)
    return n==n[::-1]

n=int(input())
while True:
    if isPrime(n) and isPalin(n):
        print(n)
        break
    else:
        n=n+1