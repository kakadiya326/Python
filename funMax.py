#find maximux using def.
def maximum(l):
    max=l[0]
    for el in l:
        if el>max:
            max=el
    return max
l=[30,45,78,34,69,28,82]
print(maximum(l))