#Variable length positional arguments
def fun(*v):
    print(v)
fun()
fun(12,56)
fun(4,7,8,23,65,87)
fun(56)