#How to write multiple exceptions in one block
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    c=a/b
    print(x)
except ValueError as v:
    print("Provide numerical values only")
except ZeroDivisionError as z:
    print("Provide non-zero values")
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("End Program")