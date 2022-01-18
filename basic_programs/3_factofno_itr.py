def factorial(n):
    if(n==1 or n==0):
        return 1
    elif(n<0):
        return 0
    else:
        fact=1
        while(n>1):
            fact*=n
            n-=1
        return fact
a=int(input("Enter a number : "))
print("The factorial of {0} is {1}".format(a,factorial(a)))
