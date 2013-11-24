from math import *

limit=2000001
crosslimit=floor(sqrt(limit-1))+1
sieve=[]

for i in range(limit):
    sieve.append('false')

i=4
while i<limit:
    sieve[i]='true'
    i=i+2

i=3
while i<crosslimit:
    if sieve[i]=='false':
        j=i*i
        while j<limit:
            sieve[j]='true'
            j=j+2*i
    i=i+2

sum=0
i=2
while i<limit:
    if sieve[i]=='false':
        sum+=i
    i=i+1

print sum
