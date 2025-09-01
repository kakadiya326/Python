n=int(input("Enter a number:"))
c=0
i=2
while True:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        c+=1
        if c==n:
            print(i)
            break
    i+=1