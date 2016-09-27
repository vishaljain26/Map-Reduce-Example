#!/usr/bin/env python
import sys

hms=[3600,60,1]
avgtime={}
count=0

def cal_seconds(time):
    time=str(time)
    seconds=sum([a*b for a,b in zip(hms,(int(i) for i in time.split(':')))])
    return seconds

for line in sys.stdin:
    line=line.strip()
    website,logintime,logoutime=line.split('\t',2)
    date, logtim = str(logintime).split(' ', 1)
    date2, logouttm = str(logoutime).split(' ', 1)
    dif = cal_seconds(logouttm) - cal_seconds(logtim)
    combo=website+','+date
    temp = []
    if (combo in avgtime.keys()):
        temp = avgtime.get(combo)
        temp.append(dif)
        avgtime[combo] = temp
    else:
        temp.append(dif)
        avgtime[combo] = temp

for key in avgtime.keys():
    sum1 = avgtime.get(key)[0]
    if (len(avgtime.get(key)) > 1):
        sum1 = 0
        temp = avgtime.get(key)
        for i in range(0, len(temp)):
            sum1 = sum1 + temp[i]
        sum1 = sum1 / (len(temp))
    avgtime[key] = sum1

for key in avgtime.keys():
    seconds=avgtime.get(key)
    key=str(key)
    website,date=key.split(',',1)
    print('%s\t%s\t%s' % (website,date,seconds))