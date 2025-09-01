#Display all prime numbers from a given list without predefine function.
l=list(map(int,input().split()))
for n in l:
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)