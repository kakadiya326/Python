s=input()
n=int(input())
ic=0
for i in range(1,len(s),2):
    ic+=int(s[i])
    if ic>n:
        print(s[s.index(s[i-1])])
        break

        
