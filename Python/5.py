import math

def prime_factor(n):
    if n%2==0:
        lastFactor=2
        while n%2==0:
            n/=2
    else:
        lastFactor=1
    factor=3
    factorSqrt=factor*factor
    while n>1 and factorSqrt<=n:
        if n%factor==0:
            lastFactor=factor
            while n%factor==0:
                n/=factor
        factor+=2
        factorSqrt=factor*factor
    if n==1:
        return lastFactor
    else:
        return n

a=20
b=a-1

while b>=1:
    if a%b!=0:
        test=prime_factor(b)
        if test==1:
            a=a*b
            print 'Testing {0}: {0} {1}'.format(b,a,b)
        else:
            a=a*test
            print 'Testing {0}: {0} {1}'.format(b,a,test)
    else:
        b=b-1

print a
