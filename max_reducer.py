#!/usr/bin/python2
##reducer to find highest Value for each Key
import sys
currentKey=""
previousKey=""
currentValue=0
currentMax=0

for line in sys.stdin:
    [currentKey, currentValue]=line.strip().split('\t')

    if previousKey and (currentKey != previousKey):
        print "{0}\t{1}".format(previousKey, currentMax)
        currentMax=0

    if currentValue > currentMax:
        currentMax=currentValue
    previousKey=currentKey


print "{0}\t{1}".format(previousKey, currentMax)
