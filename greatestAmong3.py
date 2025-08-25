a=int(input("Enter first number: "))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))
if a==b and b==c:
    print('All are equals')
elif b>a and b>c:
    print(b,' is the greatest among others')
elif a>b and a>c:
    print(a,' is the greatest among others')
else:
    print(c,' is the greatest among others')