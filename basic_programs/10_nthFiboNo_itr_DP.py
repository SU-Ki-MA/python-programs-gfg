fiboarr=[0,1]
def fibonacci(n):
    if n<=0:
        print("Invalid input")
    elif n<=len(fiboarr):
        return fiboarr[n-1]
    else:
        for i in range(len(fiboarr)-1,n-1):
            fiboarr.append(fiboarr[i]+fiboarr[i-1])
        print(fiboarr)
        return fiboarr[n-1]
print(fibonacci(10))
