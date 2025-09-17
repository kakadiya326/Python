#Display frequency count of every elements or numbers in list to dictionary
l=list(map(int,input().split()))
d={}
for el in l:
    d[el]=d.get(el,0)+1
print(d)
#Input
# 3 5 7 8 2 5 7 9 3 5 4 8 7 1 0
#Output
# {3: 2, 5: 3, 7: 3, 8: 2, 2: 1, 9: 1, 4: 1, 1: 1, 0: 1}
