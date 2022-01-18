def fibonacci(n):
    a=0
    b=1
    if n==1:
        return a
    elif n==2:
        return b
    else:
        print("range for 2 and {} : ".format(n),*range(2,n+1))
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b
print("fibonacci of 1 : ",fibonacci(1))
print("fibonacci of 2 : ",fibonacci(2))
print("fibonacci of 3 : ",fibonacci(3))
print("fibonacci of 10 : ",fibonacci(10))
