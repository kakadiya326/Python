#Reverse the file content
f=open("file3/reverse.txt","r")
s=f.read()
f.close()
f=open("file3/reverse.txt","w")
f.write(s[::-1])
f.close()