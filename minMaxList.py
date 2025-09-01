#Display minmum, maximum element from a given list without predefine function.
l=list(map(int,input().split()))
min=max=l[0]
for el in l:
    if el<min:
        min=el
    elif el>max:
        max=el
print(min,max)