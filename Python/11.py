f = open("11.txt",'r').readlines();
data = []
for line in f:
    for token in line.split(' '):
        data.append(int(token))

#print data

max = 1
for y in range(20):
    for x in range(20):
        if x<17:
            rightNum = 1
            for i in range(4):
                rightNum *= data[y*20+x+i]
            if rightNum>max:
                max = rightNum
        if y<17:
            downNum = 1
            for i in range(4):
                downNum *= data[(y+i)*20+x]
            if downNum>max:
                max = downNum
        if x<17 and y<17:
            diagNum = 1
            for i in range(4):
                diagNum *= data[(y+i)*20+x+i]
            if diagNum>max:
                max = diagNum
        if x<17 and y>3:
            diagNum = 1
            for i in range(4):
                diagNum *= data[(y-i)*20+x+i]
            if diagNum>max:
                max = diagNum
        if x>3 and y>3:
            diagNum = 1
            for i in range(4):
                diagNum *= data[(y-i)*20+x-i]
            if diagNum>max:
                max = diagNum
        if x>3 and y<17:
            diagNum = 1
            for i in range(4):
                diagNum *= data[(y+i)*20+x-i]
            if diagNum>max:
                max = diagNum

print max
