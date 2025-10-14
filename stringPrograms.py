#Check given string is palindrome or not without considering spaces and case.
# s=input().lower()
# s=s.replace(" ","")
# if s==s[::-1]:
#     print("Palindrome")
# else:
#     print("Not")

#Reverse the given string without reversing special symbols.
# s=list(input())
# i=0
# j=len(s)-1
# while i<j:
#     if not s[i].isalnum():
#         i=i+1
#     elif not s[j].isalnum():
#         j=j+1
#     else:
#         s[i],s[j]=s[j],s[i]
#         i=i+1
#         j=j-1
# print("".join(s))

#Extract all digits from a given string form the largest number.
#if no digit are there in given string print -1.
# s=input()
# l=[]
# for ch in s:
#     if ch.isdigit():
#         l.append(ch)
# if len(l)==0:
#     print(-1)
# else:
#     print("".join(sorted(l,reverse=True)))


#Form the largest possible even number From the digit of a string.
# s=input()
# l=[]
# for ch in s:
#     if ch.isdigit():
#         l.append(ch)
# if len(l)==0:
#     print(-1)
# else:
#     l.sort(reverse=True)
#     for i in range(len(l)-1,-1,-1):
#         if int(l[i])%2==0:
#             l.append(l.pop(i))
#             print("".join(l))
#             break
#     else:
#         print(-1)

#Count vowels in String
# s=input()
# c=0
# for i in 'aeiouAEIOU':
#     c=c+s.count(i)
# print(c)

#Reverse every word in string in place.
# s=input().split()
# for i in range(len(s)):
#     s[i]=s[i][::-1]
# print(" ".join(s))

#Delete two adjucent if both are same from the given string display final reduced string.
#if no character left out print empty string.
# s=list(input())
# i=0
# while i<len(s)-1:
#     if s[i]==s[i+1]:
#         s.pop(i)
#         s.pop(i)
#         i=0
#     else:
#         i=i+1
# if len(s)==0:
#     print("Empty string")
# else:
#     print("".join(s))

#Check given two strings are anagrams or not.
#(if we rearrange alphabets in one string we can able to form other.)

# Solution-1 my
# s=input()
# t=input()
# if len(s)==len(t):
#     for ch in set(s):
#         if s.count(ch)!=t.count(ch):
#             print('No')
#             break
#     else:
#         print('Yes')
# else:
#     print('no')

#Solution-2
# s1=sorted(input())
# s2=sorted(input())
# if s1==s2:
#     print("Anagram")
# else:
#     print("No")

# Solution-3
# s=input()
# t=input()
# if len(s)==len(t):
#     for ch in s:
#         t=t.replace(ch,"",1)
#     if len(t)==0:
#         print("Anagram")
#     else:
#         print("No")
# else:
#     print("No")

