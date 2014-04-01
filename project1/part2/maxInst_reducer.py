#!/usr/bin/python2
##Reducer to find the key with the most instances
import sys
currentKey=""
previousKey=""
currentValue=0
currentInstances=0
maxKey=""
maxInstances=0

for line in sys.stdin:
    [currentKey, currentValue]=line.strip().split('\t')

    if previousKey and (currentKey != previousKey):
        if currentInstances>maxInstances
            maxInstances=currentInstances
            maxKey=previousKey


    currentInstances += 1
    previousKey=currentKey

print "{0}\t{1}".format(maxKey, maxInstances)
