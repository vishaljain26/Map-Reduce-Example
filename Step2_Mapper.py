#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
    line = line.strip()
    website,date,seconds=line.split('\t',2)
    print('%s\t%s\t%s' % (website,date,seconds))