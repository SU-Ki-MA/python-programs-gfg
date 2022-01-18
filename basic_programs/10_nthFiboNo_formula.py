import math
def fibonacci(n):
    res=(((1+math.sqrt(5))**n)-((1-math.sqrt(5))**n))/((2**n)*math.sqrt(5))
    return int(res)
print(fibonacci(3))
a={i:fibonacci(i) for i in range(14)}
print(a)
