n=int(input())
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        if j==1:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    for j in range(i-1,0,-1):
        if j==1:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n-1,0,-1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        if j==1:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    for j in range(i-1,0,-1):
        if j==1:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
