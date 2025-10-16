#It will take two value and result will done with next element
#Calculate sum of list of element.
from functools import *
import math 
l=[5,8,2,6,5,4,3,9]
print(reduce(lambda x,y:x+y,l))

#Find maximum elemet from given list.
print(reduce(lambda x,y:x if x>y else y,l))

#Calculate GCD of list of numbers
print(reduce(math.gcd,l))