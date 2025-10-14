#Define isPrime() function to check given number is prime or not.
def isPrime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
print(isPrime(5))
print(isPrime(15))
print(isPrime(53))