#Check given list contains all the element increasing order or not.
l=list(map(int,input().split()))
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        print("No")
        break
else:
    print("Yes")