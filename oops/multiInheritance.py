# Multi-level Inheritance
class person:
    def __init__(self,name,age,place,gen):
        self.name=name
        self.age=age
        self.place=place
        self.gen=gen
    def display(self):
        print(self.name,self.age,self.place,self.gen,end="")
class std(person):
    def __init__(self, name, age, place, gen, sid, dept):
        super().__init__(name, age, place, gen)
        self.sid=sid
        self.dept=dept
    def display(self):
        super().display()
        print(self.sid,self.dept,end=" --> ")
class res(std):
    def __init__(self, name, age, place, gen, sid, dept,marks):
        super().__init__(name, age, place, gen, sid, dept)
        self.marks=marks
    def display(self):
        super().display()
        print(self.marks)

class emp(person):
    def __init__(self, name, age, place, gen, eid, dept, sal):
        super().__init__(name, age, place, gen)
        self.eid=eid
        self.dept=dept
        self.sal=sal
    def display(self):
        super().display()
        print(self.eid,self.dept,self.sal)

class Cast(person):
    def __init__(self, name, age, place, gen, cid, amt):
        super().__init__(name, age, place, gen)
        self.cid=cid
        self.amt=amt
    def display(self):
        super().display()
        print(self.cid,self.amt)

obj=res("Chiranj",20,"GUJ","M",101,"MCA",89)
obj1=res("Patel",23,"GUJ","M",102,"BCA",40)
emObj=emp('Kiran',23,"HYD","M",101,"AC",54000)
c1=Cast("Kiran",20,"HYD","M",101,54900)
c1.display()
emObj.display()
obj.display()
obj1.display()