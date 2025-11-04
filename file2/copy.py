#Copy the content from one to another file.
f1=open('file2/copy.txt','r')
f2=open("file2/copy1.txt","w")
f2.write(f1.read())
f1.close()
f2.close()