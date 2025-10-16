#To get the required element from a given sequence
#Extract all even number from given list.
l=[4,8,21,4,5,6,7,8]
print(list(filter(lambda x:x%2==0,l)))

#Extract only prime number from given list.
def isPrime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
l=[12,8,7,11,15,23,21,29,19,18]
print(list(filter(isPrime,l)))