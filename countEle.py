#Count how many times given element repeated within a list without predefine function
l=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(l)):
    if k==l[i]:
        c+=1
print(c)