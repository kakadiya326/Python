# find index position of a given element within a list [Linear search] 
# without predefine function
l=list(map(int,input().split()))
k=int(input())
for i in range(len(l)):
    if l[i]==k:
        print(l.index(l[i]))
        break
else:
    print('could not found!')