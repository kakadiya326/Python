#Calculate sum of list without predefine fucntion 
n=int(input("Enter length of list : "))
l=[]
for i in range(n):
    l.append(int(input()))
s=0
for el in l:
    s=s+el
print(s)