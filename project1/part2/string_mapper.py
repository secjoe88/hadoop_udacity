#!/usr/bin/python2

##Mapper that searches for a string amongst data

import sys
import argparse
import re

parser=argparse.ArgumentParser(usage='%(prog)s string', description='Prints Key/Value pair <string, 1>')
parser.add_argument("string", help="String to match")

##Mapper accepts exactly one parameter
if len(sys.argv)!=2:
    parser.print_help()
    sys.exit()
else:
    pattern=re.compile(sys.argv[1])

string=sys.argv[1]
##Parse inputed lines using regex
for line in sys.stdin:
    print "{0}\t1".format(string)    
##    ##check if line matches regex
##    match=pattern.search(line)
##    ##If so print the portion of the line that matches the regex
##    if match:
##        print "{0}\t1".format(match.string[match.start():match.end()])
