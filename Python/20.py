#factorial = 1
#for i in range(1,101):
#    factorial *= i
factorial = reduce(lambda x,y: x*y, range(1,101))

#sum = 0
#for digit in str(factorial):
#    sum += int(digit)
sum = reduce(lambda x,y: x+y, [int(i) for i in str(factorial)])

print sum
