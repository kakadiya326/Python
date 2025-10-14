#Reverse of a string using Stack
s=input()
st=[]
for ch in s:
    st.append(ch)
rev=""
while len(st)!=0:
    rev+=st.pop()
print(rev)