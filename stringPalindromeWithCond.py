s="Abc c ba"
t=" "
for i in s:
    t=i+t
print('Yes' if s.isprintable()==t.isprintable() else 'no')