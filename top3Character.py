#Display top 3 character that were repeated most frequently in a given string
s=input()
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(sorted(d.items(),key=lambda x:x[1],reverse=True)[:3])