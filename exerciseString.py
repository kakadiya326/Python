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



mail='kakadiya@gmail.com'
pre='@gmail.com'
print('valide' if mail.find(pre) > 0 else 'not')
print('valide' if mail.index(pre) > 0 else 'not')
print('valide' if mail.count(pre) > 0 else 'not')
print('valide' if len(mail.replace(pre," ")) != len(mail) else 'not')


s="heLlo To aLL of YoU"
print(s.upper())
print(s.lower())
print(s.casefold())
print(s.title())
print(s.capitalize())

s="ABCDEFGHIJK*?&%#&"
print(s.isupper())
s="ABcDEFGHIJK*?&%#&"
print(s.isupper())

s="abcdefghi&^$&"
print(s.islower())
s="abCdefg^$^&*"
print(s.islower())

s="All Of"
print(s.istitle())

s="AbcdEFGhij"
print(s.isalpha())
s="AbcdE FGhij"
print(s.isalpha())

s="79809765432"
print(s.isdigit())
print(s.isdecimal())
print(s.isnumeric())

s="AHGJHhjshbf36538"
print(s.isalnum())

s="abc%$%546456"
print(s.isprintable())
s="\n"
print(s.isprintable())

s="\n\t"
print(s.isspace())

s="567543$#%^&"
print(s.isascii())

s="abc_1"
print(s.isidentifier())
s="1ab"
print(s.isidentifier())