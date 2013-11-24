#def prime_factors(n):
#    factors=[]
#    d=2
#    while n>1:
#        while n%d==0:
#            n/=d
#        d=d+1
#        if d*d>n:
#            if n>1: 
#                factors.append(n)
#            break
#    return factors

#num=600851475143
#prime_factor_list = prime_factors(num)
#print max(prime_factor_list)

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

num=600851475143
print prime_factor(num)
