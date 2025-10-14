#Check given string is a sub-sequence of another string or not

#Solution-1
s=input()
sub=input()
c=0
for ch in sub:
    i=c
    while i<len(s):
        if ch==s[i]:
            c=i+1
            break
        i+=1
    else:
        print("Not a Subsequence")
        break
else:
    print("Subsequence")

#Solution-2
s=input()
sub=input()
i=0
for ch in sub:
    i=s.find(ch,i)
    if i==1:
        print("No")
        break
    i+=1
else:
    print('Yes')