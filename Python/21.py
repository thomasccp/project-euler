from math import *

def sumOfProperDivisors(n):
    if n==1:
        return 0
    sum = 1
    # Only need to count up to sqrt(n)
    bound = int(floor(sqrt(n)))
    # Deal with perfect square
    if bound**2==n:
        sum = sum+bound
        bound = bound-1
    # Deal with odd number which is not divisible by even numbers
    if n%2==0:
        start = 2
        step = 1
    else:
        start = 3
        step = 2
    # Add all the proper divisors
    for i in xrange(start,bound,step):
        if n%i==0:
            sum = sum+i+n/i
    return sum

sum = 0
for a in range(1,10000):
    b = sumOfProperDivisors(a)
    if b>a:
        if a==sumOfProperDivisors(b):
            sum = sum+a+b

print sum
