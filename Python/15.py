# Recursion is way too slow
#xLimit = 21
#yLimit = 21
#
#def addBranch(x,y):
#    if x==xLimit-1 and y==yLimit-1:
#        return 0
#    elif x<xLimit-1 and y<yLimit-1:
#        sum = addBranch(x+1,y)
#        sum += addBranch(x,y+1)
#        sum += 1
#    elif x==xLimit-1 and y<yLimit-1:
#        sum = addBranch(x,y+1)
#    elif x<xLimit-1 and y==yLimit-1:
#        sum = addBranch(x+1,y)
#    return sum
#        
#sum = 1+addBranch(0,0)
#print sum

# Counting Lattice Paths
# Amount m+n steps, choose m of them that are to the left, or n of them to the south
# Central Binomial Coefficients

limit = 20
temp = 1
for i in range(1,2*limit+1):
    temp *=i
    if i==limit:
        singleN = temp
    if i==2*limit:
        doubleN = temp
print doubleN/singleN/singleN

