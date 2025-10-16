#In a given Boolean sequence every element was True all() 
# will return True Otherwise False

#In a given Boolean sequence atleast one element was True any()
# will return True otherwise False.

#all()
l=[True,True,True]
print(all(l))
l=[True,False,True]
print(all(l))

#any()
l=[False,False,False]
print(any(l))
l=[False,False,True]
print(any(l))

#Check list contain all are positive numbers or not.
l=[5,8,10,12,6]
print(all(map(lambda x:x>0,l)))
l=[5,8,-10,12,6]
print(all(map(lambda x:x>0,l)))