q=[]
while True:
    print("1.enque 2.deque 3.disp 4.exit")
    ch=int(input())
    match ch:
        case 1:
            q.append(int(input()))
        case 2:
            if len(q)==0:
                print("Queue is empty")
            else:
                print(q.pop(0))
        case 3:
            if len(q)==0:
                print("Queue is empty")
            else:
                print(*q)
        case _:
            break