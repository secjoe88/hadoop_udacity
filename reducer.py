#!/usr/bin/python2
import sys
currentKey=""
previousKey=""
currentValue=0
currentTotal=0

for line in sys.stdin:
    [currentKey, currentValue]=line.strip().split('\t')

    if previousKey and (currentKey != previousKey):
        print "{0}\t{1}".format(previousKey, currentTotal)
        currentTotal=0


    currentTotal += float(currentValue)
    previousKey=currentKey


print "{0}\t{1}".format(previousKey, currentTotal)
