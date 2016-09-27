#!/usr/bin/env python
import sys
import re


for line in sys.stdin:
    line=line.strip()
    website, logintime, logoutime = line.split('\t', 2)
    print('%s\t%s\t%s' % (website,logintime,logoutime))