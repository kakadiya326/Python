#Count how many characters, words, lines available in a given file.
f=open('counterCharWrLi.txt','r')
s=f.read()
f.close()
l=s.count("\n")+1
w=s.count(" ")+l
c=len(s)-(l-1)
print(c,w,l)

f=open('counterCharWrLi.txt','r')
s=f.read()
lc=wc=c=0
f.close()
for ch in s:
    if ch =='\n':
        lc+=1
        wc+=1
    elif ch==" ":
        wc+=1
        c+=1
    else:
        c+=1
print(c,wc+1,lc+1)
