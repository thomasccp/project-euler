f = open("18.txt","r").readlines();
data = []
level = 0
for line in f:
    for token in line.split(' '):
        data.append(int(token))
    level += 1

totalNum = (1+level-1)*(level-1)/2

sum = []
for i in range(totalNum):
    sum.append(0);

currLevel = level
while currLevel>1:
    startIdx = (1+currLevel-1)*(currLevel-1)/2
    for i in range(currLevel-1):
        if currLevel==level:
            if data[startIdx+i]>data[startIdx+i+1]:
                sum[startIdx+i-currLevel+1] = data[startIdx+i]+data[startIdx+i-currLevel+1]
            else:
                sum[startIdx+i-currLevel+1] = data[startIdx+i+1]+data[startIdx+i-currLevel+1]
        else:
            if sum[startIdx+i]>sum[startIdx+i+1]:
                sum[startIdx+i-currLevel+1] = sum[startIdx+i]+data[startIdx+i-currLevel+1]
            else:
                sum[startIdx+i-currLevel+1] = sum[startIdx+i+1]+data[startIdx+i-currLevel+1]
    currLevel -= 1

print sum
