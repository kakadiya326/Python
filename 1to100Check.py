#check if all elements are between 1 and 100
l=list(map(int,input().split()))
for el in l:
    if el<1 or el>100:
        print("No")
        break
else:
    print("Yes")