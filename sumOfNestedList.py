#Sum of nested list which contains elements and sublists
#Input Format: [1,2,[3,4],5,6,[7,8]]
#Output Format: 36
l=eval(input())
s=0
for i in l:
    if type(i)==list:
        for j in i:
            s=s+j
    else:
        s=s+i
print(s)