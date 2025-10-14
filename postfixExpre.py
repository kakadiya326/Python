#Pass given postfix expression from left to right.
#If it is operand push into the stack.
#If it is operator pop most top 2 symbol stack perform the intended operation.
#  push back result to a stack.
s=input()
st=[]
for ch in s:
    if ch.isdigit():
        st.append(int(ch))
    else:
        b=st.pop()
        a=st.pop()
        match ch:
            case '+':
                x=a+b
            case '-':
                x=a-b
            case '*':
                x=a*b
            case '%':
                x=a%b
        st.append(x)
print(st[::])
            
            