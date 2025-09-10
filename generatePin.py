# from the given mx4 matrix generate 5 digit pin first for digit are maximum 
# from every column, last digit pf minimum of all the column.

n=int(input())
l=[]
for i in range(n):
    x=[]
    for j in range(4):
        x.append(int(input()))
    l.append(x)
pin=0
min=max=l[0][0]
for j in range(4):
    max=l[0][j]
    for i in range(n):
        if l[i][j]>max:max=l[i][j]
        if l[i][j]<min:min=l[i][j]
    pin=pin*10+max
pin=pin*10+min
print(pin)