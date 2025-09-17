#Addition of Matrix
r=int(input())
c=int(input())
A=[[int(input()) for j in range(c)] for i in range(r)]
B=[[int(input()) for j in range(c)] for i in range(r)]
C=[[A[i][j]+B[i][j] for j in range(c)] for i in range(r)]
print("Output:",C)