n=int(input('Enter a number : '))
count=0
for i in range(1,n):
    if n%i==0:
        count+=i
        print(i)
print('Total factoes : ',count)
if count==n:
    print(n,' is perfect fectoes') 
elif count<n:
    print(n,' is deficient')
elif count>n:
    print(n,' is abundant')