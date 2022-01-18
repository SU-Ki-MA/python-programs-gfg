def fact(n):
    if(n==1 or n==0):
        return 1
    elif(n<0):
        return 0
    else:
        return n*fact(n-1)
a=int(input("Enter a number : "))
print(fact(a))
