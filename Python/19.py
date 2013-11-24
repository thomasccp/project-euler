days = [31,28,31,30,31,30,31,31,30,31,30,31]
daysLeap = [31,29,31,30,31,30,31,31,30,31,30,31]

dayCount = 0
sunCount = 0
for year in range(1901,2000):
    for month in range(12):
        if dayCount%7==6:
            sunCount += 1
        if year%400!=0 and year%4==0:
            dayCount += daysLeap[month]
        else:
            dayCount += days[month]

print sunCount
