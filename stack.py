#Implemention of Stack
st=list(map(int,input().split()))
while True:
    print("1.push 2.pop 3.peek 4.exit")
    ch=int(input())
    match ch:
        case 1:
            st.append(int(input()))
        case 2:
            if len(st)==0:
                print("Underflow")
            else:
                print(st.pop())
        case 3:
            if len(st)==0:
                print('Stack is empty')
            else:
                print(st[-1])
        case _:
            break
