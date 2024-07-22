x=int(input("enter 1st num:"))
y=int(input("enter 2st num:"))

def gcd(x,y):
    #method 1
    fx=[]
    fy=[]

    for i in range(1,x+1):
        if (x%i)==0:
            fx.append(i)

    for i in range(1,y+1):
        if (y%i==0):
            fy.append(i)

    cf=[]
    for f in fx:
        for g in fy:
            if f==g:
                cf.append(f)

    print ("gcd:",max(cf))

def hcf(x,y):
    #method 2
    z=min(x,y)
    for i in range(1,z+1):
        if (x%i==0 and y%i==0):
            hcf=i

    print ("hcf=",hcf)

#method 3
def gcd1(x,y):
    i=min(x,y)
    while i>0:
        if(x%i==0 and y%i==0):
            gcd1=i
            break
        else:
            i=i-1
    print("gcd1:",gcd1)

gcd(x,y)
hcf(x,y)
gcd1(x,y)
