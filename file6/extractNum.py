#Extract all numerical values from a given file.
f=open('extraxtNum.txt','r')
s=f.read()
f.close()
l=[]
num=''
for ch in s:
    if ch.isdigit():
        num=num+ch
    else:
        if len(num)!=0:
            l.append(num)
            num=""
if len(num)!=0:
    l.append(num)
print(l)