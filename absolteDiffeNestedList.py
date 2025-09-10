#Calculate absolute difference between sum of direct element in a given square matrix.
#Solution-1 (my)

l=[[1,2,3],[4,5,6],[7,8,9]]
left=0
right=0
for i in range(len(l)):
    for j in range(len(l)):
        if i==j:
            left+=l[i][j]
    for j in range(len(l)-1,-1,-1):
        if i==j:
            right+=l[i][j]
print(left,right)

#Solution-2 
n=int(input())
l=[]
for i in range(n):
    x=[]
    for j in range(n):
        x.append(int(input()))
    l.append(x)
ps=os=0
for i in range(n):
    ps+=l[i][i]
    os+=l[i][n-i-1]
print("reuslt : ",abs(ps-os))