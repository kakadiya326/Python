#Reverse the string
s='Hello'
r=''
for ch in s:
    r=ch+r
print(r)
r=''
for ch in range(len(s)-1,-1,-1):
    r=r+s[ch]
print(r)

print(s[::-1])
