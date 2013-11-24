limit=4000000
first=2
second=8
sum=first
while(second<limit):
    sum+=second
    temp=second
    second=4*second+first
    first=temp
print sum

#sum=0
#first=1
#second=1
#while(second<4000000):
#    if(second%2==0):
#        sum+=second
#    temp=second
#    second=first+second
#    first=temp
#print sum
