#Generate 1 to n number.
def fun(n):
    for i in range(1,n+1):
        yield i
print(list(fun(8)))


def fun1(s):
    for ch in s:
        yield "-".join(ch)
print(list(fun1('hello')))

def fun1(s):
    yield "-".join(s)
print(list(fun1('hello')))