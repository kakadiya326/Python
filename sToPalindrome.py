s=input()
c=0
i=0
j=len(s)-1
while i<j:
    c=c+abs(ord(s[i])-ord(s[j]))
    i+=1
    j-=1
print(c)