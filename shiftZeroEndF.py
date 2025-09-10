#Shift all zero to ending from a given list
#solution-1
s1=list(map(int,input().split()))
i=0
for _ in range(len(s1)):
    if s1[i]==0:
        s1.append(s1.pop(i))
    else:
        i+=1
print(s1)

#solution-2
s2=list(map(int,input().split()))
i=0
for j in range(len(s2)):
    if s2[j]!=0:
        s2[i],s2[j]=s2[j],s2[i]
        i+=1
print(s2)