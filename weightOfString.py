#Calculate weight of string
s='abcdefghijklmnopqrstuvwxyz'
weight=0
for ch in s:
    weight+=ord(ch)-96
print('Weight of string is:',weight)