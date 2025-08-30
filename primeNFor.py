#display prime numbers between 1 to n using nested for loops
n= int(input("Enter a number: "))
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

