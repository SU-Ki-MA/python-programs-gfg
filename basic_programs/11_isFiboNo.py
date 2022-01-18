import math
def isPerfectSquare(a):
    s=int(math.sqrt(a))
    return s*s==a
def isFibonacci(b):
    return isPerfectSquare(5*b*b-4) or isPerfectSquare(5*b*b+4)
for i in range(1,15):
    print(i," is fibonacci") if isFibonacci(i) else print(i," is not fibonacci")
