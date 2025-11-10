#Read data from file and take one empty list and create one 
# obj std class after that append in list
class std:
    def __init__(s,sid,name,dept,mark):
        s.sid=sid
        s.name=name
        s.dept=dept
        s.mark=mark
    def __str__(s):
        return f"{s.sid}, {s.name}, {s.dept}, {s.mark}"
    
f=open("data.txt","r")
l=[]
x=f.readlines()
for row in x:
    t=row.strip().split()
    l.append(std(int(t[0]),t[1],t[2],int(t[3])))
