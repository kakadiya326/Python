#Create a student class that contain stdID, name, dept, 4 sub marks, as a data members
# get total, get percentage, display as a member function.

class std:
    def __init__(self,sid,name,dept,s1,s2,s3,s4):
        self.sid=sid
        self.name=name
        self.dept=dept
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
    def display(self):
        print(self.sid,self.name,self.dept,self.s1,self.s2,self.s3,self.s4)

    def getTotal(self):
        return self.s1+self.s2+self.s3+self.s4
    def getPercentage(self):
        return "{:.2f}%".format(self.getTotal()/4)

std1=std(101,"Chiranj","MCA",90,90,90,90)
std2=std(102,"Kakadiya","MCA",40,40,40,40)
std1.display()
std2.display()
print(std1.getTotal())
print(std2.getTotal())
print(std1.getPercentage())
print(std2.getPercentage())