#Combine two list
l=[3,6,8,3,9]
m=[7,1,2,8]
print("l + m : ",l+m) #return new list
l.extend(m)
print("extend function : ") #add list at last
print(l)