from math import *

def isPrime(num):
    if num%3==0:
        return 0
    elif num<9:
        return 1
    else:
        i=5
        rootNum=floor(sqrt(num))
        while i<=rootNum:
            if num%i==0 or num%(i+2)==0:
                return 0
            else:
                i=i+6
        return 1

num=5
sum=2+3
limit=2000000

while num<limit:
    if isPrime(num):
        sum+=num
    num=num+2
    if isPrime(num):
        sum+=num
    num=num+4

print sum
