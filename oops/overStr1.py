#Display all student data without disp method declaration.
class A:
    def __init__(s,sid,name,dept):
        s.sid=sid
        s.name=name
        s.dept=dept
    def __str__(s):
        return f"{s.sid}, {s.name}, {s.dept}"
obj=A(101,"Chiranj","ECE")
print(obj)