#Check given string contains all alphabets or not.

#Solution-1
s='abcdefghijklmnopqrstuvwxyz'

for i in range(97,123):
    if chr(i) not in s:
        print(chr(i),' is not string')
        break
else:
    print('All alphabets are present in string')

#Solution -2
s=input()
for ch in 'abcdefghijklmnopqrstuvwxyz':
    if ch not in s:
        print(ch,' is not string')
        break
else:
    print('All alphabets are present in string')