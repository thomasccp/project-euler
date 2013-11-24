from math import *

def genPrimeTable():
    sieve=[]
    crosslimit=floor(sqrt(limit-1))+1

    for i in range(limit+1):
        sieve.append('false')

    i=4
    while i<limit:
        sieve[i]='true'
        i=i+2

    i=3
    while i<crosslimit:
        if sieve[i]=='false':
            j=i*i
            while j<limit:
                sieve[j]='true'
                j=j+2*i
        i=i+2

    return sieve

def getNumDivisor(num):
    cnt = 1
    for i in range(2,limit+1):
        if sieve[i]=='false':
            if i*i>num:
                cnt = 2*cnt
                break
            exponent = 1
            while num%i==0:
                exponent = exponent+1
                num = num/i
                #print '{0} {1}'.format(num,i)
            cnt = cnt*exponent
            if num==1:
                break
    return cnt

limit=10000
sieve = genPrimeTable()
numDivisor = 0
triNum=0
cnt = 1
while numDivisor<500:
    triNum = triNum+cnt
    numDivisor = getNumDivisor(triNum)
    cnt = cnt+1
print triNum
