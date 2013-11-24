def divisibleby(num):
    bound = 999/num
    return num*(1+bound)*bound/2

print divisibleby(3)+divisibleby(5)-divisibleby(15)

#sum = 0
#for i in range(1,1000):
#    if i%3==0 or i%5==0:
#        sum += i
#print sum
