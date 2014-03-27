#!/usr/bin/python2
import sys
currentKey=""
previousKey=""
currentValue=0
currentTotal=0

for line in sys.stdin:
    [currentKey, currentValue]=line.strip().split('\t')

    if previousKey and (currentKey != previousKey):
        print "{0}\t{1}".format(currentKey, currentTotal)
        currentTotal=0
    else:
        currentTotal += float(currentValue)

    previousKey=currentKey    
