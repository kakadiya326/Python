n=int(input('Enter a number to print alternate even number : '))
alter=0
for i in range(1,n+1):
    if i%2==0:
        if alter%2==0:
            print(i)
        alter+=1