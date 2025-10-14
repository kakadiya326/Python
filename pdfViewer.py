import string
l=list(map(int,input().split()))
s=input()
d=dict(zip((string.ascii_lowercase,l)))
max=d[s[0]]
for ch in s:
    if max<d[ch]:
        max=d[ch]
print(len(s)*max)