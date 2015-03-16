#!/usr/bin/python2
##Reducer to find the number of instances of each key
import sys
currentKey=""
previousKey=""
currentValue=0
totInstances=0

for line in sys.stdin:
    [currentKey, currentValue]=line.strip().split('\t')

    if previousKey and (currentKey != previousKey):
        print "{0}\t{1}".format(previousKey, totInstances)
        totInstances=0


    totInstances += 1
    previousKey=currentKey


print "{0}\t{1}".format(previousKey, totInstances)
