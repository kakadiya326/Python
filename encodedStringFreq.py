s=input()
d={}
for i in range(0,len(s)-1,2):
    d[s[i]]=d.get(s[i],0)+int(s[i+1])
print(sorted(d.items(),key=lambda x:x[1],reverse=True)[0][0])