l=list(map(int,input().split()))
t=int(input())
i=0
j=1
print(l)
while j<=len(l):
    if l[i]+l[j]==t:
        print(i,j) 
        break
    i+=1
    j+=1