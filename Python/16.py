from sys import *

#def sumofDigits(num):
#    ln = len(str(num))
#    temp = 0
#    for i in str(ln):
#        temp += num%10
#        num /= 10
#    return temp
def sumofDigits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

if len(argv)>1:
    limit = int(argv[1])
else:
    limit = 1000
print sumofDigits(2**limit)
