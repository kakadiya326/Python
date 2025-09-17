#All set{} exericise

#Accessing set
s={4,7,2,4,6,7,8,3}
print(s) #{2, 3, 4, 6, 7, 8}
for el in s:
    print(el)
# output
# 2
# 3
# 4
# 6
# 7
# 8

print(*s) #2 3 4 6 7 8

#Add element to set
s={4,8,2,3,6,5}
s.add(1)
print(s) #{1, 2, 3, 4, 5, 6, 8}

#delete elements to set
s={4,8,2,3,6,5}
print(s.pop()) #2 #this will remove element randomly
s.remove(8) #{3, 4, 5, 6} # remove() used for specific element
print(s)

#searching
s={4,8,2,3,6,5}
print(3 in s) #True

#Set Comprehension
# s={int(input()) for i in range(6)}
print(s) #Output: {2, 3, 5, 6, 8}

#Creating empty set()
s={}
print(type(s)) #<class 'dict'>
s=set()
print(type(s)) #<class 'set'>