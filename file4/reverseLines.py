#reverse every line in a given file.
f=open("file4/reverseLines.txt","r")
l=f.readlines()
for i in range(len(l)):
    l[i]=l[i].strip()[::-1]+"\n"
l[-1]=l[-1].strip()
f.close()
f=open("file4/reverseLines.txt","w")
f.writelines(l)
f.close()