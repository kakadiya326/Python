#Abstract class and method
from abc import *
class animal(ABC):
    @abstractmethod
    def eat(s):
        pass
class cow(animal):
    def eat(s):
        print('Cow eat grass')
obj=cow()
obj.eat()