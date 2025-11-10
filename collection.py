#Protected variable declare start with single _a (single underscore).
from collections import *
s=" kk t k t s s t k"
x=Counter(s)
print(x)
print(dict(x))
print('--->',x.most_common(3))