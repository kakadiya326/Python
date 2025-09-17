#Creating dictionary from list of keys , values
k=['a','b','c','d','e','f']
v=[1,2,3,4,5,6,7,8,9]
print(list(zip(k,v))) #it will return list of tuple 
print(dict(zip(k,v))) #it will return dictionary