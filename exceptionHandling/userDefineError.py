#User define custom error.
try:
    age=int(input())
    if age<=0 or age>100:
        raise Exception("Age value 1 to 100")
    else:
        print(age)
except Exception as e:
    print(e)