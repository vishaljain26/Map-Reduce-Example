#!/usr/bin/env python
import sys

avgtime={}
result={}
predif=0
predate=0
count=0
preweb=''

for line in sys.stdin:
    line=line.strip()
    website,date,seconds=line.split('\t',2)
    avgtime[website+','+date]=seconds

timestamps=[]
for key in avgtime.keys():
    timestamps.append(key)

keys=list(sorted(timestamps, key=lambda d: tuple(map(str, d.split('-')))))
for i in range(0,len(keys)):
    keys[i]=str(keys[i])
    website,date=keys[i].split(',',1)
    date=str(date)
    yy,mm,dd=date.split('-',2)
    dd=int(dd)
    if(dd==predate+1):
        if (website == preweb):
            if (avgtime.get(keys[i]) >= preval * 2):
                count += 1
            else:
                count = 0
        if (count >= 2):
            if (website in result.keys()):
                result[website] = int(result.get(website)) + 1

            else:
                result[website] = 1

    preval = avgtime.get(keys[i])
    preweb = website
    predate= dd
for key in result.keys():
    print('%s\t%s' % (key,result.get(key)))