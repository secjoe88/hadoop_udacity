#!/usr/bin/python2
##reducer to simply regurgitate inpute key/value pairs
import sys
key=""
value=""
for line in sys.stdin:
	[key, value]=line.strip().split('\t')
	print "{0}\t{1}".format(key, value)
