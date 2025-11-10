#Define a abstract class called shape that contain area 
# as abstract method get d1,d2 as a concrete method.
from abc import *
class shape(ABC):
    def __init__(s,d1,d2=0):
        s.d1=d1
        s.d2=d2
    def getD1(s):
        return s.d1
    def getD2(s):
        return s.d2
    @abstractmethod
    def area(s):
        pass

class rect(shape):
    def area(s):
        return s.getD1()*s.getD2()

class tra(shape):
    def area(s):
        return 0.5*s.getD1()*s.getD2()

class circle(shape):
    def area(s):
        return f"{3.14*s.getD1()*s.getD1():.2f}"

r=rect(5,8)
t=tra(5,7)
c=circle(12)
print(r.area())
print(t.area())
print(c.area())