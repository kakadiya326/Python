# use of destructured assignment to initialize lists
# demonstrates aliasing problem
l=[0]*5
print(l)

l[2]=12
print(l)

l=[[0]*3 for i in range(4)] #no aliasing problem
print(l)
l[2][1]=12
print(l)

l=[[0]*3]*4 #aliasing problem
print(l)

l[2][1]=12
print(l)