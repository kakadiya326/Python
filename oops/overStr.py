#To provide custom decription for the object we need to override __str__(s) method.
class A:
    def __str__(self):
        return f"Class A obj {self}"
obj1=A()
print(obj1)