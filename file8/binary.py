#Handling the binary file creating the copy of existing image.
f=open('Kids\' Hoodie.webp','rb')
f1=open('copyFile.jpg','wb')
f1.write(f.read())
f1.close()
f.close()