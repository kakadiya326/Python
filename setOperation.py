#some basic set() operation


#Union

s1={5,8,12,4,9}
s2={8,1,2,5,9,7}
print(s1|s2)
print(s1.union(s2))
s1.update(s2)
print(s1)
#Output : {1, 2, 4, 5, 7, 8, 9, 12}

#Intersection
s1={5,8,12,4,9}
s2={8,1,2,5,9,7}
print(s1&s2)
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
#Output : {8, 9, 5}

#Difference
s1={5,8,12,4,9}
s2={8,1,2,5,9,7}
print(s1-s2)
print(s1.difference(s2))
s1.difference_update(s2)
print(s1)
#Output : {4, 12}

#Symmetric difference
s1={5,8,12,4,9}
s2={8,1,2,5,9,7}
print(s1^s2)
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)
#Output : {1, 2, 4, 7, 12}

#SubSet and SuperSet
s1={5,8,12,4,9}
s2={8,5,12}
print(s2<s1) #True
print(s2.issubset(s1))  #True
print(s1>s2) #True
print(s1.issuperset(s2)) #True
#Output : {1, 2, 4, 7, 12}

#Dis-join
s1={4,7,6}
s2={1,2,3}
print(s1.isdisjoint(s2)) #True