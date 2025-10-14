#Define is Palindrom() function to verify given number is Pl=alindrom or not.
def isPalin(s):
    n=str(s)
    return n==n[::-1]
print(isPalin(345543))