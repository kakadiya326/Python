# for i in range(20,31):
#     if i%3==0 and i%4==0:
#         break
#     print(i)
    
m = int(input())
n=int(input())
for i in range(m,n+1):
    if i%3==0 and i%5==0:
        print(i)
        break
else:
    print('No 3 and 5 multiple found')
