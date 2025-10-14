#Extract the highest length sub-string that contain unique characters.
s=input()
f=False
for k in range(len(s),0,-1):
    for i in range(0,len(s)-k+1):
        t=s[i:i+k]
        if len(t)==len(set(t)):
            print(t)
            f=True
            break
    if f: break