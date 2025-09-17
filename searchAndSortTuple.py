#Searching and Sorting in tuple
t=(5,7,3,2,8,6,7)
print(6 in t) #True
print(t.index(8)) #4
print(t.count(8)) #1
print(sorted(t)) #[2, 3, 5, 6, 7, 7, 8]
print(sum(t),min(t),max(t)) #38 2 8