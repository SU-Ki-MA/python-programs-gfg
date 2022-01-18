def findPosition(k,n):
    a=0
    b=1
    l=2
    while l!=0:
        c=a+b
        a=b
        b=c
        if b%k==0:
            return l*n
        l+=1
    return -1
n=5
k=4
print("Position of {}'th multiple of {} in Fibonacci series is : ".format(n,k),findPosition(k,n))
