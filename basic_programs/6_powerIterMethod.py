def power(x,y):
    res=1
    while(y>0):
        if((y&1)==1):
            res=res*x
        y=y>>1
        x=x*x
    return res

x=5
y=3
print(power(5,3))
