content = open("names.txt", 'r').read()
names = sorted(content.replace("\"","").split(','), key=str.upper)

total = 0
for count,str in enumerate(names):
    sum = 0
    for c in str:
        sum += ord(c)-64
    total += (count+1)*sum

print total
