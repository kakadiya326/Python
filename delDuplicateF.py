#Delete duplicate elements in list by maintain insertion order.
#solution-1
s1=[4,7,9,3,6,9,3,1,7,9,4,2,6,8,4,2]
print(list(set(s1))) #This will not maintain insertion order.

#solution-2
s2=[4,7,9,3,6,9,3,1,7,9,4,2,6,8,4,2]
r=[]
for el in s2:
    if el not in r:
        r.append(el)
print(r)

#solution-3
s3=[4,8,4,2,8,9,6,4,3,5,7,9,3,2,6,8]
i=0
while i<len(s3)-1:
    j=i+1
    while j<len(s3):
        if s3[i]==s3[j]:
            del s3[j]
        else:
            j=j+1
    i=i+1
print(s3)