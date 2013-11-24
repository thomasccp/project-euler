def test(a,sum):
    b=1
    while b<=(sum-a)/2:
        c=1000-a-b
        if a*a+b*b!=c*c:
            b=b+1
        else:
            return b
    return 0
    
a=1
sum=1000
while a<=(sum-3)/3:
    value=test(a,sum)
    if value==0:
        a=a+1
    else:
        #print '{0} {1} {2}'.format(a,value,1000-a-value)
        print a*value*(1000-a-value)
        break
