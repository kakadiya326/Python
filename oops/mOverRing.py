#If both parent and child class having same method name,
#parent class method fun overridden by child class.
class animal:
    def talk(s):
        print("Animals will give sound")
class dog(animal):
    def talk(s):
        print("Dogs will Bark")
d=dog()
d.talk()
