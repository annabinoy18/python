m=int(input("enter the 1 num:"))
n=int(input("enter the 2nd num:"))

def gcd(m,n):
    if(m<n):
        (m,n)=(n,m)
    if(m%n)==0:
        return(n)
    else:
        diff=m-n
        return(gcd(max(n,diff),min(n,diff)))
#more efficient   
def gcd1(m,n):
    if(m<n):
        (m,n)=(n,m)
    while (m%n) !=0:
        (m,n)=(n,m%n)
    return (n)
