#Find minimum and maximum in a nested list
l=[[1,2,3],[4,5],[6,7,8,9],[10]]
min=max=l[3][0]
for el in range(len(l)):
    for i in range(len(l[el])):
        if l[el][i]<min:
            min=l[el][i]
        elif l[el][i]>max:
            max=l[el][i]
print(max,min)