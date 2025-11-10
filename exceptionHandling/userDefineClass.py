#User define error using class
class AgeException(Exception):
    def __init__(s,msg="Age Error rised"):
        s.msg=msg
    def __str__(s):
        return s.msg
    
try:
    age=int(input())
    if age<=0 or age>100:
        raise AgeException()
    else:
        print(age)
except Exception as e:
    print(e)