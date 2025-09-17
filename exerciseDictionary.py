#Exercise of Dictionary
d={"name":"chiranj","age":23,"dept":"MCA","marks":90}
print(d) #{'name': 'chiranj', 'age': 23, 'dept': 'MCA', 'marks': 90}

#To add or update key value d[key]=Value
d={"name":"chiranj","age":20,"dept":"MCA","marks":90}
d["place"]="HYD"
d["age"]=23
print(d)
#Output : {'name': 'chiranj', 'age': 23, 'dept': 'MCA', 'marks': 90, 'place': 'HYD'}

#To Accessing perticular key value d[key] or d.get(key,defualtValue)
#d[key] if given key not available throws error KeyError
#get() will return default given value.
print(d['name']) #chiranj
print(d.get('name',-1)) #chiranj
#print(d['profession']) #KeyError
print(d.get('profession',-1)) #-1


#To access all the keys from given dictionary
d={"name":"chiranj","age":23}
print(d.keys()) #dict_keys(['name', 'age'])
print(d.values()) #dict_values(['chiranj', 23])
print(d.items()) #dict_items([('name', 'chiranj'), ('age', 23)])

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for k,v in d.items():
    print(k,'-->',v)

d={"name":"chiranj","age":23,"city":"amreli","dept":"MCA"}
print(d.pop('name')) # it will remove the given key value paire
print(d.popitem()) # it will remove arbitory (rondomely) value

#dictionary comprehension
d={input():int(input()) for i in range(5)}
print(d) #{'a1': 1, 'b1': 2, 'c1': 3, 'd1': 4, 'e1': 5}

