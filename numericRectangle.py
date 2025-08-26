n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i if i<j else j,end=" ")
    for j in range(n-1,0,-1):
        print(i if i<j else j,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n+1):
        print(i if i<j else j,end=" ")
    for j in range(n-1,0,-1):
        print(i if i<j else j,end=" ")
    print()