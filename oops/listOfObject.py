class std:
    def __init__(s,sid,name,dept,mark):
        s.sid=sid
        s.name=name
        s.dept=dept
        s.mark=mark
    def __str__(s):
        return f"{s.sid}, {s.name}, {s.dept}, {s.mark}"
    def __let__(s,o):
        return s.mark<o.mark
    
n=int(input())
l=[]
for i in range(n):
    l.append(std(int(input("ID : ")),input("Name : "),input("Dept : "),int(input("Marks :"))))

l.sort()
for obj in l:
    print(obj)
