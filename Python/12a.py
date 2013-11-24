from math import *

def getNumDivisor(num):
    cnt = 0
    sqrtNum = int(sqrt(num))
    for factor in range(1,sqrtNum+1):
        if num%factor==0:
            cnt = cnt+2
    if factor*factor==num:
        cnt = cnt-1
    return cnt

numDivisor = 0
triNum=0
cnt = 1
while numDivisor<500:
    triNum = triNum+cnt
    numDivisor = getNumDivisor(triNum)
    cnt = cnt+1
print triNum
