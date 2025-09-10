#Rotate k len elements from left to right.
l=list(map(int,input().split()))
k=int(input())%len(l)
for i in range(k):
    l.append(l.pop(0))
print(l)