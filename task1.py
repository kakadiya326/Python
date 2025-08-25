m=int(input('Enter starting value : '))
n=int(input('Enter ending value : '))

for i in range(m,n+1):
    s=i**0.5
    if s*s==i:
        print(i,' is perfect square')
        break
else:
    print('-1')