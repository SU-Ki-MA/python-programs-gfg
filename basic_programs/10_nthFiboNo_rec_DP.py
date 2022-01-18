fibarr=[0,1]
def fibonacci(n):
    if n<=0:
        print("Incorrect input for fibonacci function")
    elif n<=len(fibarr):
        return fibarr[n-1]
    else:
        temp_fib=fibonacci(n-1)+fibonacci(n-2)
        fibarr.append(temp_fib)
        return temp_fib
print(fibonacci(100))
print(fibarr)
