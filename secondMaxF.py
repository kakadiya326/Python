#Find second largest element from a given list
#solution-1
s1=[3,6,7,36,7,3,67,8,4,34,65]
s1=sorted(set(s1),reverse=True)
print(s1[1])

#solution-2
s2=[23,6,34,75,23,75,3,6,3,7]
max1=max2=s2[0]
for el in s2:
    if el>max1:
        max2,max1=max1,el
    elif el!=max1 and el>max2:
        max2=el
print(max2)
