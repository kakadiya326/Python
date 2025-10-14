#Balancing Paranthesis
s=input()
st=[]
for ch in s:
    if ch in '({[':
        st.append(ch)
    else:
        if len(st)==0:
            print('Not Balanced')
        else:
            if st[-1]=='{' and ch == '}':
                st.pop()
            elif st[-1]=='[' and ch == ']':
                st.pop()
            elif st[-1]=='(' and ch == ')':
                st.pop()
            else:
                print('Not Balanced')
                break
else:
    if len(st)==0:
        print("Balanced")
    else:
        print('Not Balanced')