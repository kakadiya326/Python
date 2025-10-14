#To remove leading and trailing spaces
s="   Hello   to    "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

#To remove leading and trailing characters
s="ababaacbabacbabaa"
print(s.strip('ab'))
print(s.lstrip('ab'))
print(s.rstrip('ab'))

#To remove prefix and suffix
s="abccbd"
print(s.removeprefix('abc'))
print(s.removesuffix('cbd'))

#To check starting and ending of a string
s="hello"
print(s.startswith('he'))
print(s.endswith('lo'))

#To align the string
s="Hello to all"
print('{:*<20s}'.format(s))
print('{:*>20s}'.format(s))
print('{:*^20s}'.format(s))
print('{:*^20.5s}'.format(s))

#To give justification
s="Hello to all"
print(s.ljust(20,'*'))
print(s.rjust(20,'*'))
print(s.center(20,'*'))
print(s[:3].center(20,'*'))

s="677667"
print(s.zfill(10))


#To formate() to string data
a,b,c=11,22,33
print("a={0},b={1},c={2}".format(a,b,c))
print("a={2},b={1},c={0}".format(a,b,c))

#Partition will return three tokens in tuple by any way 
#If no sub-string found then it will return one main-string and two empty string
s="abcabdacabdag"
print(s.partition("abd"))
print(s.rpartition("abd"))
print(s.partition("abdk"))

#By help of given string how many times 'irsr' can form.
# s=input()
ic=s.count('i')
rc=s.count('r')//2
sc=s.count('s')
print(min(ic,rc,sc))

#By help of given string how many times given sub-string can form
# s=input()
# sub=input()
# d={}
# for ch in set(sub):
#     d[ch]=s.count(ch) // sub.count(ch)
# print(min(d.values()))

#String base data numerical sorting.
l=['23','12','1','89','234','26','9','456','43','47','1867']
l.sort(key=lambda x:(len(x),x))
print(l)

l=['html','css','js','java','react','express']
print(max(l,key=lambda x: len(x)))
print(sorted(l,key=lambda x: len(x))[-1])