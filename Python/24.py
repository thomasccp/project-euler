from math import *

# For number start with 0, i.e. 0XXXXXXXXXX
# There are 9!=362881 permutations
# 0XXXXXXXXXX is the 1st to the 362881st numbers
# 1XXXXXXXXXX is the 362882nd to 725760th numbers
# The 1000000th number should start with 2

level = 9
bound = 1000000
value = 0
digitList = [0,1,2,3,4,5,6,7,8,9]
while level>=0:
    print digitList
    
    numOfPerm = factorial(level)
    idx = int((bound-1)/numOfPerm)
    startDigit = digitList[idx]
    print "numOfPerm: {0}  idx: {1}  startDigit: {2}  bound: {3}".format(numOfPerm, idx, startDigit, bound)
    
    value = value+startDigit*10**level
    digitList.remove(startDigit)
    level = level-1
    bound = bound%numOfPerm
    print "====="

print value
