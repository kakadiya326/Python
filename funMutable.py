#If you pass mutable object as argument modification did on formal parameter will
# reflect to actual parameter.
def fun(l):
    l.append(12)
    l.insert(2,8)
    l.pop(0)
    l=l[3:] #Before this all modification occured in 
            #   main object but when list is re-initialize 
            #   list reference changed
    l[2]=45
    print(l)
x=[8,5,6,9,18,25,3,7]
fun(x)
print(x)