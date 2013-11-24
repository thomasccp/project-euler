#def reverseInt(num):
#    return int(str(num)[::-1])
def reverseInt(num):
    reversed=0
    while num>0:
        reversed=reversed*10+num%10
        num/=10
    return reversed

def test(dividend,divisor):
    quotient = dividend/divisor
    if dividend%divisor==0 and quotient>99 and quotient<1000:
        #print '{0} {1}'.format(divisor, dividend/divisor)
        return 1
    else:
        return 0

pattern=989
upper=pattern
lower=reverseInt(pattern)
divisor=999
while test(upper*1000+lower,divisor)==0:
    if(divisor>=501): 
        divisor=divisor-1
    else:
        pattern=pattern-1
        upper=pattern
        lower=reverseInt(pattern)
        divisor=999

print upper*1000+lower
