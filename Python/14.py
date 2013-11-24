limit = 1000000
biggestCnt = 1
biggestIdx = 1
cache = []

for i in range(limit+1):
    cache.append(-1)

cache[1] = 1
for start in range(2,limit+1):
    cnt=1
    num=start
    while num!=1 and num>=start:
        if num%2==0:
            num = num/2
        else:
            num = 3*num+1
        cnt = cnt+1
    cache[start] = cnt+cache[num]
    if cache[start]>biggestCnt:
        biggestCnt = cache[start]
        biggestIdx = start

print '{0} {1}'.format(biggestCnt,biggestIdx)
