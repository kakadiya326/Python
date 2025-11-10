# Create a employee class that contains employee id, name, dept, salary, as
# a default member display as a member function.

class emp:
    def __init__(self,eid,name,dept,sal):
        self.eid=eid
        self.name=name
        self.dept=dept
        self.sal=sal
    def display(self):
        print(self.eid,self.name,self.dept,self.sal)

e1=emp(101,"Salary","AC",35000)      
e2=emp(102,"Shiv","ME",150000)      
e3=emp(101,"Shakti","MCA",20000)      
e1.display()
e2.display()
e3.display()
print(e1.eid)
e1.sal=20
e1.display()