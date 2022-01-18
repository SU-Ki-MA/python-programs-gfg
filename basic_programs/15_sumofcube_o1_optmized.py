def sumOfCubes(n):
    x=0
    if n%2==0:
        x=(n/2)*(n+1)
    else:
        x=((n+1)/2)*n
    return (int) (x*x)
print(sumOfCubes(5))
