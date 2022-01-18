import math
def checkPrime(a):
    if a>1:
        for i in range(2,math.ceil(math.sqrt(a))+1):
            if a%i==0 and a!=i:
                return False
        else:
            return True
b=int(input("Enter a number : "))
if(checkPrime(b)):
    print("Given number is Prime")
else:
    print("Given number is not Prime")
