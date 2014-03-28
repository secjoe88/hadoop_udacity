#!/usr/bin/python2
## Reducer to find total number of keys and sum of their values
import sys
totKeys =0
valueTotal=0

for line in sys.stdin:
    totKeys+=1
    valueTotal+=float(line.strip().split('\t')[1])

print "{0}\t{1}".format(totKeys, valueTotal)
