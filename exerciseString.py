#To access character by character
s='Hello'
for i in range(len(s)):
    print(s[i])

for ch in s:
    print(ch)

#To know wether sub-string available within main-string or not membership operator will use.
s="Hello to all"
print("to" in s)
print("too" in s)

#To know the index position of a given sub-string
s="aabcaababcadabcac"
sub="abc"
print(s.index(sub)) 
print(s.find(sub))   
print(s.rindex(sub))
print(s.rfind(sub))
print(s.index(sub,3,10))
print(s.find(sub,3,8))

s='abacabcacacb'
print(s.count('ac'))
print(s.count('acb'))

s="Hello to all welcome to all"
print(s.split())
print(s.rsplit())
print(s.split(" ",3))
print(s.rsplit(" ",3))
s='12-06-2003'
print(s.split("-"))
s="12,45,43,65,54,6743"
print(s.split(","))
print(s.split())

s="acabca dabcrsdfabcx"
print(s.split("abc"))

l=["Hello","to","all","welcome","to","all"]
print(" ".join(l))

l=['1','2','3','4','5','6','7','8']
print("".join(l))

s="acabcadabccdabad"
print(s.replace("abc","*"))
print(s.replace("abc","*",1))
print(s.replace("abc",""))
print(s.replace("xabc"," "))

s="Hello"
print(list(s))