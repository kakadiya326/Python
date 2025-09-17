r1=int(input())
c1=int(input())
r2=int(input())
c2=int(input())
if c1==r2:
    A=[[int(input()) for j in range(c1)] for i in range(r1)]
    B=[[int(input()) for j in range(c2)] for i in range(r2)]
    C=[]
    for i in range(r1):
        x=[]
        for j in range(c2):
            s=0
            for k in range(c1):
                s=s+A[i][k]*B[k][j]
            x.append(s)
        C.append(x)
    print("Output:",C)#Multiplication of Matrix
else:
    print("Invalid input")#Multiplication of Matrix