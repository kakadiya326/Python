#Reverse the given list
l=[5,7,3,7,9,12,4]
print(l[::-1]) # This creates a new list, it does not modify the original list.
l.reverse() # it modifies the original list itself, No new list is created.
print(l)