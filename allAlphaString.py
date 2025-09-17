#Check given string contains all alphabets or not.

s='abcdefghijklmnopqrstuvwxyz'

for i in range(97,123):
    if chr(i) not in s:
        print(chr(i),' is not string')
        break
else:
    print('All alphabets are present in string')