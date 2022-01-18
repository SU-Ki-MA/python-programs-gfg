import math
def prime(x,y):
    prime_list=[]
    for i in range(x,y):
        if i==0 or i==1:
            continue
        else:
            print(*range(2,math.ceil(math.sqrt(i))+1))
            for j in range(2,math.ceil(math.sqrt(i))+1):
                if i%j==0 and i!=j:
                    break
            else:
                prime_list.append(i)
    return prime_list
listitems=prime(2,7)
if len(listitems)==0:
    print("There are no prime numbers in this list")
else:
    print("The prime numbers are ",listitems)
