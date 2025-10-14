#(positional,default argument,keyword argument,
# variable-length positional,variable-length keyword)

def fun(a,*v,b=0,c=0,**kw):
    print(a,v,b,c,kw)
fun(3,4,7,9,2,3,9,0,4,7,5,3,1,7,5,9,k=3,s=5,b=0,w=7,h=3)