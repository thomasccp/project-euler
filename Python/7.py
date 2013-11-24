import math

def isPrime(num):
    if num%3==0:
        return 0
    else:
        i=5
        rootNum = math.floor(math.sqrt(num))
        while i<=rootNum:
            if num%i==0 or num%(i+2)==0:
                return 0
            else:
                i=i+6
        return 1

count=2
num=5
limit=10001
while count<limit:
    if isPrime(num)==1:
        count=count+1
    num=num+2
print num-2
