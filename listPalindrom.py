#Check if the elements of the list are palindromes
l = list(map(int, input().split()))

for i in l:
    temp = i 
    p = 0
    while temp != 0:
        digit = temp % 10
        p = p * 10 + digit
        temp //= 10
    if p == i:
        print(i)

