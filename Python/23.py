from math import *

def checkAbundant(n):
    if n==1:
        return False
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
    for i in xrange(start,bound+1,step):
        if n%i==0:
            sum = sum+i+n/i
            if sum>n:
                return True
                break
    return False

bound = 28123

# Generate the list of abundant numbers
#abundantList = []
#for i in range(12,bound+1):
#    if checkAbundant(i)==True:
#        abundantList.append(i)
abundantList = [i for i in range(12,bound+1) if checkAbundant(i)==True]

# Generate the check list
checkList = [False for i in range(bound)]

# Cross out the numbers that can be written as the sum of two abundant numbers
for i in range(len(abundantList)):
    for j in range(i,len(abundantList)):
        sum = abundantList[i]+abundantList[j]
        if sum<bound+1:
            checkList[sum-1] = True

sum = 0
for i in range(bound):
    if checkList[i]==False:
        sum = sum+i+1

print sum
