#display prime factors for given number n using nested for loops
n=int(input("Enter a number: "))
for i in range(2,n+1):
    if n%i==0:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
