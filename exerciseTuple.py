t=(5,12,32,8,6,7)
#Solution-1

#output
# 5
# 12
# 32
# 8
# 6
# 7
print("#Solution-1")
for i in range(len(t)):
    print(t[i])

#Solution-2
#output
# 5
# 12
# 32
# 8
# 6
# 7
print("#Solution-2")
for el in t:
    print(el)

#Solution-3
#output
# 5 12 32 8 6 7
print("#Solution-3")
print(*t)


#Creating tuple with one element
t=(5)
print(type(t)) #<class 'int'>
t=(5,)
print(type(t)) #<class 'tuple'>

#Adding
t=(5,8,7,2,3)
t=t+(12,)
print(t) #(5, 8, 7, 2, 3, 12)

#Adding specific index
t=(5,8,7,2,3)
t=t[:2]+(12,)+t[2:]
print(t) #(5, 8, 12, 7, 2, 3)

#Removing
t=(5,8,7,2,3)
t=t[:2]+t[3:]
print(t) #(5, 8, 2, 3)

#
t=(3,(4,5,6,7),4.5,[4,5,6,7],2)
#t[3]=12 #Changing element of tuple rise error because tuple is immutable
t[3][2]=12 #Changing inside element which should mutable is possible
#(3, (4, 5, 6, 7), 4.5, [4, 5, 12, 7], 2)
print(t)