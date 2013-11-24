#singleCount = ['one','two','three','four','five','six','seven','eight','nine']
#specialCount = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
#tenCount = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
singleCount = [3,3,5,4,4,3,5,5,4]
specialCount = [3,6,6,8,8,7,7,9,8,8]
tenCount = [6,6,5,5,5,7,6,6]

count = 0
for i in range(1000):
    if i>=100:
        #print '{0} {1}'.format(singleCount[i/100-1],'hundred'),
        count += singleCount[i/100-1]
        count += 7
        if i%100!=0:
            #print 'and',
            count += 3
    if i%100>=10 and i%100<20:
        #print specialCount[i%100-10]
        count += specialCount[i%100-10]
    else:
        if i%100>19:
            #print tenCount[i/10%10-2],
            count += tenCount[i/10%10-2]
        if i%10!=0:
            #print singleCount[i%10-1]
            count += singleCount[i%10-1]

#print 'one thousand'
count += 11
print count
