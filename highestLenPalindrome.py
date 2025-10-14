#Display highest length palindrome sub-string from a given string
s=input()
f=False
for k in range(len(s),0,-1):
    for i in range(0,len(s)-k+1):
        t=s[i:i+k]
        if t==t[::-1]:
            print(t)
            f=True
            break
    if f: break
